import circle # this method requires the module name to be called prior to the function used
#from circle import area, diameter # only imports specific functions and/or global variables from a module does not require calling the module name
#from circle import * # not recommended, imports all functions and global variables from the module but can lead to function name conflicts
import constants

def main():
    radius1 = 3
    area1 = circle.area(radius1)
    diameter1 = circle.diameter(radius1)

    print(f'area is: {area1: .2f}')
    print(f'diameter in: {diameter1: .2f}')
    
    # demonstrates the use of a cache for imported modules.
    # in main we import circle which in turn imports constants.
    # in main we also import and use constants.
    # however when main executes. 'in constants module' prints
    # once not twice. This is because python caches the variables
    # created in the first import of constants then subsequent uses
    # reference those cached values.  
    print(f'pi is {constants.PI}')

main()
