import os

BASE_DIR = os.getcwd()
LOG_DIR_NAME = 'sorted'
dir_path = os.path.join(BASE_DIR, LOG_DIR_NAME)
FILE_NAME_RESULT = 'result.txt'
file_path_result = os.path.join(BASE_DIR, LOG_DIR_NAME, FILE_NAME_RESULT)
files_names = sorted(os.listdir(dir_path))


def result_write(data, file_path_result):
    with open(file_path_result, 'w', encoding='utf-8') as file:
        for len_file in sorted(data):
            data_file = data[len_file]
            for num_string in range(len(data_file)):
                file.write(data_file[num_string])


def files_open(files_names):
    files_data = {}
    for file_dot_txt in files_names:
        data_file_path = os.path.join(BASE_DIR, LOG_DIR_NAME, file_dot_txt)
        if file_dot_txt != 'result.txt':
            with open(data_file_path, encoding='utf-8') as file:
                data = []
                data += [file_dot_txt + '\n'] + file.readlines()
                files_data[len(data)] = data
        else:
            pass
    return files_data


data = files_open(files_names)
result_write(data, file_path_result)