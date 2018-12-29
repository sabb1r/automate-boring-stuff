import pyperclip
import sys

text_input = pyperclip.paste()
lines = text_input.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text_output = '\n'.join(lines)
pyperclip.copy(text_output)