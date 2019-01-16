#! /usr/bin/python3

import pyperclip
import sys
import shelve

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]
    else:
        print('Wrong Input')
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf.keys():
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    else:
        print('Wrong Input')
else:
    print('You have to provide 2 or 3 command line argument')
mcb_shelf.close()
sys.exit()