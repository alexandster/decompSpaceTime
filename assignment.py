import settings

def assign(inXf, inYf, inZf, xmaxf, xminf, ymaxf, yminf, zmaxf, zminf):


    p1, p2 = settings.p1, settings.p2
    
    xr2 = (xmaxf + xminf)/2     # Subdomain division x coordinates (middle of range)
    yr2 = (ymaxf + yminf)/2     # Subdomain division y coordinates (middle of range)
    zr2 = (zmaxf + zminf)/2     # Subdomain division z coordinates (middle of range)

    sdX1, sdX2, sdX3, sdX4, sdX5, sdX6, sdX7, sdX8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (X-coordiantes)
    sdY1, sdY2, sdY3, sdY4, sdY5, sdY6, sdY7, sdY8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (Y-coordiantes)
    sdZ1, sdZ2, sdZ3, sdZ4, sdZ5, sdZ6, sdZ7, sdZ8 = [],[],[],[],[],[],[],[]    #list of data points for each subdomain (Z-coordiantes)

    for x, y, z in zip(inXf, inYf, inZf):       # assign each data point to subdomain
        if x < xr2 - p1:
            if y < yr2 - p1:
                if z < zr2 - p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                elif z < zr2 + p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                else:
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
            elif y < yr2 + p1:
                if z < zr2 - p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                elif z < zr2 + p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                else:
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
            else:
                if z < zr2 - p2:
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                elif z < zr2 + p2:
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                else:
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
        elif x < xr2 + p1:                
            if y < yr2 - p1:
                if z < zr2 - p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                elif z < zr2 + p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                else:
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
            elif y < yr2 + p1:
                if z < zr2 - p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                elif z < zr2 + p2:
                    sdX1.append(x), sdY1.append(y), sdZ1.append(z)
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
                else:
                    sdX5.append(x), sdY5.append(y), sdZ5.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
            else:
                if z < zr2 - p2:
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                elif z < zr2 + p2:
                    sdX3.append(x), sdY3.append(y), sdZ3.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
                else:
                    sdX7.append(x), sdY7.append(y), sdZ7.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
        else:
            if y < yr2 - p1:
                if z < zr2 - p2:
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                elif z < zr2 + p2:
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                else:
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
            elif y < yr2 + p1:
                if z < zr2 - p2:
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                elif z < zr2 + p2:
                    sdX2.append(x), sdY2.append(y), sdZ2.append(z)
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
                else:
                    sdX6.append(x), sdY6.append(y), sdZ6.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
            else:
                if z < zr2 - p2:
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                elif z < zr2 + p2:
                    sdX4.append(x), sdY4.append(y), sdZ4.append(z)
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)
                else:
                    sdX8.append(x), sdY8.append(y), sdZ8.append(z)

    sdXYZd = [sdX1, sdY1, sdZ1, sdX2, sdY2, sdZ2, sdX3, sdY3, sdZ3, sdX4, sdY4, sdZ4, sdX5, sdY5, sdZ5, sdX6, sdY6, sdZ6, sdX7, sdY7, sdZ7, sdX8, sdY8, sdZ8, xr2, yr2, zr2]

    return sdXYZd 

