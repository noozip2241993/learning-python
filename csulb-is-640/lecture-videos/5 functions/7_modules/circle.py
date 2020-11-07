import constants

def area(radius):
    return radius * radius * constants.PI

def diameter(radius):
    return radius * 2

def circumference(radius):
    return diameter(radius) * constants.PI

def main():
    print('Test diameter function')
    assert 6 == diameter(3) #if true nothing will happen if false will throw exception

'''
If a module is imported by another module, its __name__ has a value of the module name, i.e., the filename without the .py postfix. For example, if the circle module was imported, its __name__ has a value of circle.
If it is executed by Python interprete in command line, the __name__ has a value of __main__.
'''
if __name__ == '__main__':
    main()
