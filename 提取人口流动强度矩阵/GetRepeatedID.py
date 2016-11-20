#!python
#coding:utf-8
import copy
from multiprocessing import Process
import math
import linecache
import re
from time import ctime
import os
import traceback
#change current working directory
os.chdir('C:\ShenZhenMedicalProject\CellphoneIDList')

docs = os.listdir('C:\ShenZhenMedicalProject\CellphoneIDList')
       
class GetRepeatedID(Process):
        input_filename_1 = ''
        input_filename_2 = ''
        input_filename_3 = ''
        output_filename = ''
        def __init__(self,input_filename_1, input_filename_2, input_filename_3, output_filename):
                Process.__init__(self)
                self.input_filename_1 = input_filename_1
                self.input_filename_2 = input_filename_2
                self.input_filename_3 = input_filename_3
                self.output_filename = output_filename
        def run(self):
                print(str(self.input_filename_2) + "  begin  %s\n" %ctime())
                f_input_1 = open(self.input_filename_1, 'r')
                f_input_2 = open(self.input_filename_2, 'r')
                f_input_3 = open(self.input_filename_3, 'r')
                f_output = open(self.output_filename, 'w')

                cellphone_id_dict = {}
                try:
                        while True:
                            line = f_input_1.readline()
                            if len(line) == 0:
                                break;
                            line_split = line.split(',')
                            key = line_split[0] + ',' + line_split[1] + ',' + line_split[2]
                            if cellphone_id_dict.has_key(key) == False:
                                cellphone_id_dict[key] = int(line_split[3])
                            else:
                                cellphone_id_dict[key] += 1

                        while True:
                            line = f_input_2.readline()
                            if len(line) == 0:
                                break;
                            line_split = line.split(',')
                            key = line_split[0] + ',' + line_split[1] + ',' + line_split[2]
                            if cellphone_id_dict.has_key(key) == False:
                                cellphone_id_dict[key] = int(line_split[3])
                            else:
                                cellphone_id_dict[key] += 1

                        while True:
                            line = f_input_3.readline()
                            if len(line) == 0:
                                break;
                            line_split = line.split(',')
                            key = line_split[0] + ',' + line_split[1] + ',' + line_split[2]
                            if cellphone_id_dict.has_key(key) == False:
                                cellphone_id_dict[key] = int(line_split[3])
                            else:
                                cellphone_id_dict[key] += 1
                except Exception:
                        traceback.print_exc()


                for key in cellphone_id_dict.keys():
                    if int(cellphone_id_dict[key]) != 0:
                        f_output.write(str(key) + ',' + str(cellphone_id_dict[key]) + '\n')
                f_output.close()

                print(str(self.output_filename) +"  finish  %s\n" %ctime())
                
                
if __name__=='__main__':
    
        plist = []
        i = 2
        while(i <= 47):
                proc = GetRepeatedID('CellphoneIDList' + str(i-1) + '.txt', 'CellphoneIDList' + str(i) + '.txt', 'CellphoneIDList' + str(i+1) + '.txt', 'RepeatedID' + str(i) + '.csv')
                plist.append(proc)
                i = i+1
        for proc in plist:
                proc.start()
        for proc in plist:
                proc.join()

        input()
