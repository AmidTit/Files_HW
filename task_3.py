import os

FILE_NAME = ['1.txt', '2.txt', '3.txt']
RESULT_FILE = 'result.txt'
FILE_DIR = '2.4.files'
FILE_SUB_DIR = 'sorted'
ROOT_PATH = os.getcwd()

path_1 = os.path.join(ROOT_PATH, FILE_DIR, FILE_SUB_DIR, FILE_NAME[0] )
path_2 = os.path.join(ROOT_PATH, FILE_DIR, FILE_SUB_DIR, FILE_NAME[1] )
path_3 = os.path.join(ROOT_PATH, FILE_DIR, FILE_SUB_DIR, FILE_NAME[2] )
path_result = os.path.join(ROOT_PATH, FILE_DIR, FILE_SUB_DIR, RESULT_FILE )

with open(path_1, encoding = 'utf-8') as file_1:
    file_1 = file_1.readlines()
    len_f_1 = len(file_1)
    file_1[-1] += '\n'
    
    
with open(path_2, encoding = 'utf-8') as file_2:
    file_2 = file_2.readlines()
    len_f_2 = len(file_2)

with open(path_3, encoding = 'utf-8') as file_3:
    file_3 = file_3.readlines()
    len_f_3 = len(file_3)

with open(path_result, 'a', encoding = 'utf - 8') as result_file:
    files_list = [file_1, file_2, file_3]
    files_list.sort()
    count = -1
    for element in files_list:
       result_file.write("Имя файла")
       result_file.write('\n' + str(len(files_list[count]))+ '\n')
       result_file.writelines(files_list[count])
       count -= 1
    


    
   

