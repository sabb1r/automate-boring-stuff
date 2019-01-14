#! /usr/bin/python3

import pyperclip
import sys
import shelve

mcb_shelf = shelve.open('mcb')
if len(sys.argv) < 2:
    print('Wrong Input. Required at least one input but 0 given.')
    sys.exit()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) ==2 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcb_shelf.keys())))
elif len(sys.argv) == 2 and sys.argv[1] in mcb_shelf.keys():
    pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
    