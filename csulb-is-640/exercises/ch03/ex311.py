'''Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of 
several tankfuls of gasoline by recording miles driven and gallons used for each tankful. Develop a 
sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons used 
for each tankful. The script should calculate and display the miles per gallon obtained for each tankful. 
After processing all input information, the script should calculate and display the combined miles per 
gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).'''

#initialization
tot_mile_driven = 0
tot_gal_used = 0
this_mile_driven = 0
this_gal_used = 0

#processing
while this_gal_used != -1:
    this_gal_used = float(input('Enter the gallons used (-1 to end): '))
    if this_gal_used != -1:
        this_mile_driven = float(input('Enter the miles driven: '))
        print(f'The miles/gallon for this tank was {this_mile_driven / this_gal_used:.6f}')
        tot_gal_used += this_gal_used
        tot_mile_driven += this_mile_driven
    
#termination
print(f'The overall average miles/gallon was {tot_mile_driven / tot_gal_used:.6f}')