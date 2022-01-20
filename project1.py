import pathlib
import time
import os
def eligible_files():
    file_name = input()
    if 'D ' in file_name:
        file_name = file_name.replace('D ', '')
        content = os.listdir(file_name)
        names_string = []
        for file in content:
            path_of_file = f'{file_name}\\{file}'
            if os.path.isfile(path_of_file):
                    names_string.append(f'{file_name}\\{file}')
        for word in sorted(names_string):
            print(word)
            
    elif 'R ' in file_name:
        file_name = file_name.replace('R ', '')
        content = os.listdir(file_name)
        names = []
        sec_names = []
        for file in content:
            path_of_file = f'{file_name}\\{file}'
            if os.path.isfile(path_of_file):
                    names.append(f'{file_name}\\{file}')
            else:
                sub = os.listdir(f'{file_name}\\{file}')
                for sub_file in sub:
                    path_of_sub = f'{file_name}\\{file}\\{sub_file}'
                    if os.path.isfile(path_of_sub):
                        sec_names.append(f'{file_name}\\{file}\\{sub_file}')
        for word in sorted(names):
            print(word)
        for string in sorted(sec_names):
            print(string)
    elif 'N ' in file_name:
        file_name = file_name.replace('N ', '')
        data = []
        for root, directory, files in os.walk('C:'):
            if file_name in files:
                data.append(os.path.join(root, file_name))
        for variable in sorted(data, reverse = True):
            print(os.path.abspath(variable))
    elif 'E ' in file_name:
        file_name = file_name.replace('E ', '')
        data = []
        for root, directory, files in os.walk('C:'):
            if file_name in files:
                data.append(os.path.join(root, file_name))
        for variable in sorted(data, reverse = True):
            print(variable)
    elif file_name == 'A':
        print('All files found are interesting')
    elif file_name == 'F':
        file_list = []
        file_lists = []
        for root, directory, files in os.walk('C:'):
            for file in files:
                if file.endswith('.txt'):
                    file_list.append(os.path.join(root, file))
        for element in file_list:
            file_lists.append(os.path.abspath(element))
        for files in sorted(file_lists, reverse = True):
            file_content = open(f'{files}')
            for num in range(1):
                lines = file_content.readline()
                print(lines)
    else:
        print('ERROR')
        file_name = eligible_files()
        return file_name
while True:
    eligible_files()

    
