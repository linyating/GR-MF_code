import os
import copy

os.chdir('C:\ShenZhenMedicalProject')

LU_ID = open('C:\ShenZhenMedicalProject\LU2ID_2.csv', 'r')
H_ID = open('C:\ShenZhenMedicalProject\Hospital2ID_2.csv', 'r')
F_LU_list = open('C:\ShenZhenMedicalProject\LUAndNearByCellSites.csv', 'r')
F_H_list = open('C:\ShenZhenMedicalProject\Hospital&NearbyCellSite.csv', 'r')

R = open('C:\ShenZhenMedicalProject\R.csv', 'w')

LU_lines = LU_ID.readlines()
H_lines = H_ID.readlines()[0:3]

LU_list = F_LU_list.readlines()
H_list = F_H_list.readlines()

H = []
LU = []
temp = {}
result = []

error = 0
sum_entries = 0;
#initialize result[]
for i in range(3):
    result.append([])
    for j in range(803):
        result[i].append(0)

#initialize H[]
for i in range(len(H_lines)):
    H_line_split = H_lines[i].split(',')
    H.append({})
    for j in range((len(H_line_split)-1)/2):
        if(H[i].has_key(H_line_split[j*2+1])):
            H[i][H_line_split[j*2+1]] += int(H_line_split[j*2+2])
            error += 1
        else:
            H[i][H_line_split[j*2+1]] = int(H_line_split[j*2+2])
    #print len(H[i]),(len(H_line_split)-1)/2

#init5ialize LU[]          
for i in range(len(LU_lines)):
    LU_line_split = LU_lines[i].split(',')
    LU.append({})
    for j in range((len(LU_line_split)-1)/2):
        if(LU[i].has_key(LU_line_split[j*2+1])):
            LU[i][LU_line_split[j*2+1]] += int(LU_line_split[j*2+2])
        else:
            LU[i][LU_line_split[j*2+1]] = int(LU_line_split[j*2+2])
    #print len(H[i]), (len(LU_line_split)-1)/2
    


for i in range(len(H)):
    for j in range(len(LU)):
        fre_sum = 0
        #x = -1
        #y = -1
        for key in LU[j].keys():
            if(H[i].has_key(key)):
                fre_sum += int(LU[j][key]) + int(H[i][key])
        #find the right place for row H[i]
        '''
        for s in range(len(H_list)):
            if(H_list[s][0] == H_lines[i][0]):
               x = s
        for s in range(len(LU_list)):
            if(LU_list[s][0] == LU_lines[j][0]):
               y = s
        if x == -1 or y == -1:
               print(i, j, 'error')
        else:
            result[i][j] = fre_sum
            print i, j
        '''
        result[i][j] = fre_sum
        print i, j

#print result

for i in range(len(result)):
    for j in range(len(result[i])-1):
        R.write(str(result[i][j]) + ',')
    R.write(str(result[i][-1]) + '\n')

R.close()
LU_ID.close()
H_ID.close()
F_LU_list.close()
F_H_list.close()




                   

    
