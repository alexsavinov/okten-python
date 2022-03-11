# есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com
#
import re

input_file_name = 'emails.txt'
output_file_name = 'emails_parsed.txt'

try:
    with open(input_file_name, 'r') as input_file:
        with open(output_file_name, 'w') as output_file:
            for line in input_file:
                match = re.search(r'[A-z0-9\._]+@gmail\.com', line)
                if match is not None:
                    output_file.write(f'{match.group(0)}\n')
    print(f'New file: {output_file_name}')
except FileNotFoundError:
    print(f'File {input_file_name} not found!')
except Exception as err:
    print(err)
