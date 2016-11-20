import os
import re
#to differentiate float numbers
pattern = re.compile('^\d+(\.\d+)?$',re.S)

#change current working directory
#os.chdir('C:\\Users\\wz\\Desktop\\深圳医疗项目\\data')
os.chdir('C:\\ShenZhenMedicalProject\\NewMedicalData')

#get documents of current directory and remove this python file
docs = os.listdir('C:\\ShenZhenMedicalProject\\NewMedicalData')
#docs.remove('ExtractLivingUnits.py')
#docs.remove('GetMatrix.py')
docs.remove('result.csv')
#docs.remove('Matrix.csv')
#docs.remove('FinalMatrix.csv')
#docs.remove('LivingUnit&Frequency.csv')


LivingUnits = open('result.csv', 'r')

LivingUnitsList = LivingUnits.readlines()

Matrix = []
for i in range(len(docs)):
    vector = [0]*(len(LivingUnitsList))
    f = open(docs[i], 'r')
    
    print(docs[i])
    lines = f.readlines()
    
    for line in lines:
        #get latitude and longitude and check if they are float numbers
        #print(line)
        lat = line.split(',')[9]
        lgt = line.split(',')[10]
        match_lat = pattern.match(lat)
        match_lgt = pattern.match(lgt)
        
        #if they are float numbers put them into the result list
        if match_lat and match_lgt:
            float_lat = ("%.2f" % float(lat))
            float_lgt = ("%.2f" % float(lgt))
            entry = str(float_lat) + ',' + str(float_lgt) + '\n'
            vector[LivingUnitsList.index(entry)] = vector[LivingUnitsList.index(entry)] + 1
    Matrix.append(vector)
    #print(len(vector))
    f.close()
    print(float((i+1))/len(docs))
    

f_out = open('NewMatrix.csv', 'w')

for row in Matrix:
    for i in range(len(row)-1):
        #print(len(row))
        f_out.write(str(row[i]) + ',')
    f_out.write(str(row[len(row)-1]) + '\n')
f_out.close()

    
                

                
