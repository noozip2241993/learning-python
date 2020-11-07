'''
From:
https://github.com/ying-teaching/python/blob/master/5-functions/function-concepts.md

'''

def goodIsOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False

    print('Unreachable')

def betterIsOdd(number):
    # because the function returns a bool value
    # the for loop in goodIsOdd is not necessary
    # both return the same result, this is just
    # simpler.
    result = number % 2 == 1
    return result
print(goodIsOdd(5))
print(betterIsOdd(5))
