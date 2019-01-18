import re

with open('random.txt', 'r') as f:
    text = f.read()

word_list = text.split(' ')

pattern = re.compile(r'(NOUN|ADJECTIVE|VERB|ADVERB)')

for ind, word in enumerate(word_list):
    mo = re.search(pattern, word)
    if mo:
        inp = input(f'Enter an {word}: ')
        word = re.sub(pattern, inp, word)
        print(word)
        word_list[ind] = word

new_text = ' '.join(word_list)
print(new_text)

