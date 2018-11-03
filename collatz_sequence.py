def collatz(number):
    '''This function returns half of given number if it is even otherwise three times plus one of the given number'''
    if number%2 == 0:
        res = number // 2
    else:
        res = 3*number + 1
    
    print(res)
    return res

num = input('Enter an integer: ')
try:
    num = int(num)

    cltz = collatz(num)
    while cltz != 1:
        cltz = collatz(cltz)

except ValueError:
    print("You have to enter an integer.")

