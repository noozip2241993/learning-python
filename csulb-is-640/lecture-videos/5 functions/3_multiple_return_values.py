'''
From:
https://github.com/ying-teaching/python/blob/master/5-functions/function-concepts.md

'''

def get_name():
    first = input('First name? ')
    second = input('Second name? ')
    return (first, second)
first_name, second_name = get_name()
print(first_name, second_name)

