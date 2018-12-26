def present(l):
    if len(l) == 0:
        return ''
    elif len(l) == 1:
        return l[0]
    else:
        first_segment = ', '.join(l[:-1])
        last_segment = ' and ' + l[-1]
        return first_segment + last_segment

spam = ['banana', 'orange']
print(present(spam))