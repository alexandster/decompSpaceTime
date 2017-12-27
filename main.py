#import modules
from datetime import datetime
import sys, os
import decomposition as decomp, settings as sett

#set recursion limit
sys.setrecursionlimit(4000)

#initialize global variables
sett.init()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#read parameters
pFile = open('files/parameterFile.txt', "r")
pFile.readline()
pList = pFile.readline().split("\t")

sett.p1 = float(pList[0])	# p1 = spatial bandwidth
sett.p2 = float(pList[1])	# p2 = temporal bandwidth
sett.p3 = float(pList[2])	# p3 = spatial resolution
sett.p4 = float(pList[3])	# p4 = temporal resolution
sett.p5 = float(pList[4])	# p5 = number of points threshold (T1)
sett.p6 = float(pList[5])	# p6 = buffer ratio threshold (T2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create output directory
sett.dir1 = 'pointFiles'
if not os.path.exists(sett.dir1):
    os.makedirs(sett.dir1)

sett.dir2 = 'timeFiles'
if not os.path.exists(sett.dir2):
    os.makedirs(sett.dir2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#read input point file
pFile = open('files/data.txt', "r")
inX, inY, inZ = [], [], []
r = pFile.readline().split(",")
xmin, xmax, ymin, ymax, zmin, zmax = float(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5].strip())

for record in pFile:   
	inX.append(float(record.split(",")[0]))
	inY.append(float(record.split(",")[1]))
	inZ.append(float(record.split(",")[2]))
    
pFile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#start decomposition
startTime = datetime.now()
decomp.decompose(inX, inY, inZ, xmin, xmax, ymin, ymax, zmin, zmax)
endTime = datetime.now()

#record decomposition time
runTime = endTime - startTime 
tFile=open('timeFiles/decomp_time.txt', "w")
tFile.write(str(runTime))
tFile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











