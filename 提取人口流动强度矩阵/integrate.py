import os

os.chdir('C:\ShenZhenMedicalProject\RepeatedCellphoneIDList')

docs = os.listdir('C:\ShenZhenMedicalProject\RepeatedCellphoneIDList')

docs.remove('Hospital&NearbyCellSite.csv')
docs.remove('Hospital2ID.csv')
docs.remove('IntegratedCellPhoneData.csv')

f_out = open('IntegratedCellPhoneData.csv', 'w')

IdAndLocList = {}

for i in range(46):
    f = open('RepeatedID'+ str(i+2) + '.csv', 'r')
    lines = f.readlines()
    for j in range(len(lines)):
        line = lines[j].split(',')
        key = line[0] + ',' + line[1] + ',' + line[2]
        fre = line[3]
        if IdAndLocList.has_key(key):
            IdAndLocList[key] = IdAndLocList[key] + int(fre)
        else:
            IdAndLocList[key] = 0
    print(i, len(docs))
    f.close()

for i in IdAndLocList.keys():
    f_out.write(str(i) + ',' + str(IdAndLocList[i]) + '\n')

f_out.close()
