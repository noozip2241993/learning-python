'''In the code below

    for ***:
        for ***:
            print('@')
        print()

replace the *** so that when you execute the code, it displays two rows, each containing seven @ symbols, as in:
@@@@@@@
@@@@@@@'''

for row in range(2):
    for col in range(7):
        print('@', end='')
    print()