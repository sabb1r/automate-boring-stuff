import re
import os

user_input = input('Enter a regex expression: ')
pattern = re.compile(r'{}'.format(user_input))

txt_files = [x for x in os.listdir() if x.endswith('.txt')]

for file in txt_files:
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        if re.search(pattern, line):
            print(line, end=' ')
    print('\n')
    f.close()


