ExtractLivingUnits.py
该文件用于提取居住区。文件的输入为原始医疗数据，输出为result.csv

GetMatrix.py
该文件用于提取原始X矩阵。输入为原始医疗数据和result.csv；输出为csv文件，内容是X矩阵，每一项为某居住区到某医院的就诊人次。

normalization.py
该文件用于对原始X矩阵进行归一化。输入为原始X矩阵的csv文件，输出为归一化后的X矩阵。