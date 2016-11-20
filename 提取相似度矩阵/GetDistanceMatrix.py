# -*- coding: cp936 -*-
import os
import re
import math
from math import exp

pattern = re.compile('^\d+(\.\d+)?$',re.S)
os.chdir('C:\ShenZhenMedicalProject')

#维度一度对应距离为111.32km，经度一度对应距离为102.715km

f = open('LUAndNearByCellSites.csv', 'r')
f_out = open('DistanceMatrix_LU_pure.csv', 'w')
LivingUnits = f.readlines()

DistanceMatrix = []

for i in range(len(LivingUnits)):
    vector = []
    for j in range(len(LivingUnits)):
        lat_of_point1 = LivingUnits[i].split(',')[0]
        lgt_of_point1 = LivingUnits[i].split(',')[1]

        lat_of_point2 = LivingUnits[j].split(',')[0]
        lgt_of_point2 = LivingUnits[j].split(',')[1]

        distance = math.sqrt(math.pow((math.fabs(float(lat_of_point1)-float(lat_of_point2))*111.32),2) + math.pow((math.fabs(float(lgt_of_point1)-float(lgt_of_point2))*102.715), 2))
        if i != j:
            vector.append(distance)
            
        else:
            vector.append(0)
    for k in range(len(vector) - 1):
        f_out.write(str(vector[k])[0:7] + ',')
    f_out.write(str(vector[-1])[0:7] + '\n')
    print(i)

f.close()
f_out.close()

        
