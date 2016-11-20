import os
import math
#change current working directory
os.chdir('C:\ShenZhenMedicalProject\FormerWorks')

f_matrix = open('Matrix.csv', 'r')

f_frequency = open('LivingUnit&Frequency.csv', 'r')
f_out = open('FinalMatrix.csv', 'w')

matrix_lines = f_matrix.readlines()
matrix = []

frequency_lines = f_frequency.readlines()

for i in range(len(matrix_lines)):
	vector = matrix_lines[i].split(',')
	
	for j in range(len(vector)):
		#vector[j] = int(vector[j])/int(frequency_lines[j].split(',')[2])
	        if vector[j]!=0:
                        vector[j]=math.log(int(vector[j]))
		#print(vector, frequency_lines[j][1])
		

	matrix.append(vector)
#print(matrix)
f_matrix.close()
f_frequency.close()


for row in matrix:
    for i in range(len(row)-1):
        f_out.write(str(row[i]) + ',')
    f_out.write(str(row[len(row)-1]) + '\n')
f_out.close()

