'''
Please write a program that use nested loop to draw the following pattern. 

-	You must use nested loop to draw the pattern 
-	Define and use the ROWS = 30 constant to draw the pattern for 30 rows.
-	Each row has a row number that has a width of 4 and is right aligned. 
-	There a space after the row number, followed by the first # char.
-	From the 2nd row, each row has one more space between the two # chars. 2nd row has one space char, 3rd row has two space chars, and so on and so forth. The 30th row has 29 space chars.

   1 ##
   2 # #
   3 #  #
   4 #   #
   5 #    #
   6 #     #
   7 #      #
   8 #       #
   9 #        #
  10 #         #
… (your program should draw all rows from 1 to 30)
29 #                            #
30 #                             #
'''

DRAW_CHAR = '#'
ROWS = 30
LEFT_POS = 0
RIGHT_POS = 0

for row in range(ROWS):
    print(f'{row + 1:>4} ', end='') # print this row's number as specified
    RIGHT_POS += 1 # set this row's right position
    for col in range(ROWS + 1):
        if col == LEFT_POS or col == RIGHT_POS:
            print(DRAW_CHAR, end='') # print the DRAW_CHAR if we are at either the left or right positions
        else:
            print(' ', end='') #otherwise print a space
    print() #end the row