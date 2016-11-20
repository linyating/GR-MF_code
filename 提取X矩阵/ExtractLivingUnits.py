import os
import re
#to differentiate float numbers
pattern = re.compile('^\d+(\.\d+)?$',re.S)

#change current working directory
os.chdir('C:\\Users\\wz\\Desktop\\深圳医疗项目\\data')

#get documents of current directory and remove this python file
docs = os.listdir()
docs.remove('result.csv')
docs.remove('FinalMatrix.csv')
docs.remove('Matrix.csv')
docs.remove('LivingUnit&Frequency.csv')
#read every file and generate a list of every living units
result = []

i = 0
for i in range(len(docs)):
    f = open(docs[i], 'r')
    print(docs[i])
    lines = f.readlines()
    for line in lines:
        try:
            lat = line.split(',')[9]
            lgt = line.split(',')[10]
            match_lat = pattern.match(lat)
            match_lgt = pattern.match(lgt)
            #if they are float numbers put them into the result list
            if match_lat and match_lgt:
                float_lat = ("%.3f" % float(lat))
                float_lgt = ("%.3f" % float(lgt))
                entry = str(float_lat) + ',' + str(float_lgt)+'\n'
            #check if they are already in the list
                if result.count(entry) == 0:
                    result.append(entry)
        except Exception:
            print(line)
    f.close()
    print((i+1)/len(docs))

    
#put results into result.csv
f_out = open('result.csv', 'w')
for entry in result:
    f_out.write(entry)
f_out.close()

            

