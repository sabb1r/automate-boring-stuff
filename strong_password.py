import re

def is_strong(pswd):
    '''This function will check whether pswd is strong or weak'''
    
    if len(pswd) < 8:
        return False
    elif not re.compile(r'[A-Z]').search(pswd):
        return False
    elif not re.compile(r'[a-z]').search(pswd):
        return False
    elif not re.compile(r'\d').search(pswd):
        return False
    else:
        return True


password = input('Enter your password: ')
if is_strong(password):
    print('Your password is strong.')
else:
    print('Your password is weak.')
