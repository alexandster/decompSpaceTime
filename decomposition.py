import assignment as ass, settings as sett, os

def decompose(inXd, inYd, inZd, xmind, xmaxd, ymind, ymaxd, zmind, zmaxd):    # inXd: list of x-coordinates \ inYd: list of y-coordinates \ inZd: list of z-coordinates
                                                                                                                    # xmind: subdomain lower x boundary \ xmaxd: subdomain upper x boundary \ ymind: subdomain lower x boundary
                                                                                                                    # ymaxd: subdomain upper y boundary \ zmind: subdomain lower x boundary \ zmaxd: subdomain upper z boundary
                                                                                                                    # xybufd: spatial buffer \ zbufd: temporal buffer
                                                                                                                 
    sett.sdNum += 1
    
    xminDiff = xmind%sett.p3
    xmaxDiff = xmaxd%sett.p3
    yminDiff = ymind%sett.p3
    ymaxDiff = ymaxd%sett.p3
    zminDiff = zmind%sett.p4
    zmaxDiff = zmaxd%sett.p4

    xminP = xmind - xminDiff + sett.p3
    xmaxP = xmaxd - xmaxDiff + sett.p3
    yminP = ymind - yminDiff + sett.p3
    ymaxP = ymaxd - ymaxDiff + sett.p3
    zminP = zmind - zminDiff + sett.p4
    zmaxP = zmaxd - zmaxDiff + sett.p4

    xC, yC, zC = 0,0,0

    xIter = xminP
    while xIter < xmaxP:
        xC += 1
        xIter += sett.p3

    yIter = yminP
    while yIter < ymaxP:
        yC += 1
        yIter += sett.p3

    zIter = zminP
    while zIter < zmaxP:
        zC += 1
        zIter += sett.p4

    xDim = xmaxd - xmind
    yDim = ymaxd - ymind
    zDim = zmaxd - zmind

    sdVolume = xDim * yDim * zDim
    bufVolume = (xDim + 2 * sett.p1) * (yDim + 2 * sett.p1) * (zDim + 2 * sett.p2) 
    bufRatio = sdVolume / bufVolume

    if len(inXd) is 0:    # if there are no data points or no regular grid points within subdomain, pass
        pass
    elif xC is 0:
        pass
    elif yC is 0:
        pass
    elif zC is 0:
        pass
    elif len(inXd) <= sett.p5 or bufRatio <= sett.p6:

		fn = sett.dir1 + os.sep + "pts_" + str(sett.sdNum) + ".txt"
		fn1 = open(fn, "w")
                fn1. write(str(xmind) + ", " + str(xmaxd) + ", " + str(ymind) + ", " + str(ymaxd) + ", " + str(zmind) + ", " + str(zmaxd) + "\n")
		for x, y, z in list(zip(inXd, inYd, inZd)):
			fn1.write(str(x) + ", " + str(y) + ", " + str(z) + "\n")
		fn1.close()
            
    else:   # if number of points in subdomain is higher than threshold, keep decomposing.
        sdXYZ = ass.assign(inXd, inYd, inZd, xmaxd, xmind, ymaxd, ymind, zmaxd, zmind)        
        decompose(sdXYZ[0], sdXYZ[1], sdXYZ[2], xmind, sdXYZ[-3], ymind, sdXYZ[-2], zmind, sdXYZ[-1])      # recursive function call 1
        decompose(sdXYZ[3], sdXYZ[4], sdXYZ[5], sdXYZ[-3], xmaxd, ymind, sdXYZ[-2], zmind, sdXYZ[-1])      # recursive function call 2
        decompose(sdXYZ[6], sdXYZ[7], sdXYZ[8], xmind, sdXYZ[-3], sdXYZ[-2], ymaxd, zmind, sdXYZ[-1])      # recursive function call 3
        decompose(sdXYZ[9], sdXYZ[10], sdXYZ[11], sdXYZ[-3], xmaxd, sdXYZ[-2], ymaxd, zmind, sdXYZ[-1])    # recursive function call 4
        decompose(sdXYZ[12], sdXYZ[13], sdXYZ[14], xmind, sdXYZ[-3], ymind, sdXYZ[-2], sdXYZ[-1], zmaxd)   # recursive function call 5
        decompose(sdXYZ[15], sdXYZ[16], sdXYZ[17], sdXYZ[-3], xmaxd, ymind, sdXYZ[-2], sdXYZ[-1], zmaxd)   # recursive function call 6
        decompose(sdXYZ[18], sdXYZ[19], sdXYZ[20], xmind, sdXYZ[-3], sdXYZ[-2], ymaxd, sdXYZ[-1], zmaxd)   # recursive function call 7
        decompose(sdXYZ[21], sdXYZ[22], sdXYZ[23], sdXYZ[-3], xmaxd, sdXYZ[-2], ymaxd, sdXYZ[-1], zmaxd)   # recursive function call 8




