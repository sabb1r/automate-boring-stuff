#! /usr/bin/python3

# An insecure password manager
# The passwords listed here are fake of course.

import pyperclip
import sys

pswd = {'gmail': 'slitjowij23452', 'facebook': 'iotjadkomn##532', 'yahoo': 'iwejhtrj6549684'}

if len(sys.argv) < 2:
    print('You have to enter the account name the password of which you want to know.')
    sys.exit()
else:
    account = sys.argv[1]

if account in pswd.keys():
    pyperclip.copy(pswd[account])
    print('The password of the account {} is copied to clipboard'.format(account))
else:
    print('The password of the account {} is not found in the database'.format(account))



