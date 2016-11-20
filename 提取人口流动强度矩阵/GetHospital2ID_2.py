import os

os.chdir('C:\ShenZhenMedicalProject')

cellphoneData = open('C:\ShenZhenMedicalProject\IntegratedCellPhoneData.csv', 'r')
cellSiteData = open('H_CellSites.csv', 'r')
f_out = open('Hospital2ID_2.csv', 'w')

cellphoneRecords = cellphoneData.readlines()
cellSiteRecords = cellSiteData.readlines()

result = {}

for i in range(len(cellphoneRecords)):
    cellphoneRecord = cellphoneRecords[i].split(',')
    key = str("%.3f" % float(cellphoneRecord[1])) + ' ' + str("%.3f" % float(cellphoneRecord[2]))
    fre = int(cellphoneRecord[3])
    for j in range(len(cellSiteRecords)):
        cellSiteRecord = cellSiteRecords[j].split(',')
        cellSiteLoc = cellSiteRecord[0]
        if key == cellSiteRecord[0]:
            #print cellphoneRecord, cellSiteRecord
            for k in range(len(cellSiteRecord)-1):
                
                H_loc = cellSiteRecord[k+1]
                if H_loc[-1] == '\n':
                    H_loc = H_loc[0:-1]
                if result.has_key(H_loc):
                    result[H_loc].append([cellphoneRecord[0], str(fre)])
                else:
                    result[H_loc] = []
                    result[H_loc].append([cellphoneRecord[0], str(fre)])
                '''
                print k, cellSiteRecord[k+1]
                if result.has_key(cellSiteRecord[k+1]):
                    result[cellSiteRecord[k+1]].append([cellphoneRecord[0], str(fre)])
                else:
                    result[cellSiteRecord[k+1]] = []
                    result[cellSiteRecord[k+1]].append([cellphoneRecord[0], str(fre)])
                '''
    if i % 1000000 == 0:
        print(i, len(cellphoneRecords))

#print result
for k in result.keys():
    if(str(k)[-1] == '\n'):
        f_out.write(str(k)[0:-1] + ',')
    else:
        f_out.write(str(k) + ',')
    for t in range(len(result[k])):
        f_out.write(result[k][t][0] + ',' + result[k][t][1] + ',')
    f_out.write('\n')

cellphoneData.close()
cellSiteData.close()
f_out.close()
    
