import re

def reg_strip(text, sep=' '):
    pattern1 = re.compile(r'^\s*')
    output = pattern1.sub('', text)
    pattern2 = re.compile(r'\s*$')
    output = pattern2.sub('', output)
    return output

print(reg_strip('   Hello World         '))

