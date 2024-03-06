def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as txt_file:
        txt_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as txt_file:
        txt_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", 'r') as txt_file:
        for line in txt_file:
            return line
