'''(Simulation: The Tortoise and the Hare) In this problem, you’ll re-create the classic race 
of the tortoise and the hare. You’ll use random-number generation to develop a simulation of 
this memorable event.

Our contenders begin the race at square 1 of 70 squares. Each square represents a
position along the race course. The finish line is at square 70. The first contender to reach
or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its
way up the side of a slippery mountain, so occasionally the contenders lose ground.

A clock ticks once per second. With each tick of the clock, your application should
adjust the position of the animals according to the rules in the table below. Use variables
to keep track of the positions of the animals (i.e., position numbers are 1–70). Start each
animal at position 1 (the “starting gate”). If an animal slips left before square 1, move it
back to square 1.

Animal      Move type   Percentage of the time  Actual move
Tortoise    Fast plod   50%                     3 squares to the right
            Slip        20%                     6 squares to the left
            Slow plod   30%                     1 square to the right
Hare        Sleep       20%                     No move at all
            Big hop     20%                     9 squares to the right
            Big slip    10%                     12 squares to the left
            Small hop   30%                     1 square to the right
            Small slip  20%                     2 squares to the left

Create two functions that generate the percentages in the table for the tortoise and
the hare, respectively, by producing a random integer i in the range 1 ≤ i ≤ 10. In the
function for the tortoise, perform a “fast plod” when 1 ≤ i ≤ 5, a “slip” when 6 ≤ i ≤ 7 or
a “slow plod” when 8 ≤ i ≤ 10. Use a similar technique in the function for the hare.

    Begin the race by displaying
        BANG !!!!!
        AND THEY'RE OFF !!!!!

Then, for each tick of the clock (i.e., each iteration of a loop), display a 70-position line
showing the letter "T" in the position of the tortoise and the letter "H" in the position of
the hare. Occasionally, the contenders will land on the same square. In this case, the tortoise 
bites the hare, and your application should display "OUCH!!!" at that position. All
positions other than the "T", the "H" or the "OUCH!!!" (in case of a tie) should be blank.
After each line is displayed, test for whether either animal has reached or passed
square 70. If so, display the winner and terminate the simulation. If the tortoise wins, display 
TORTOISE WINS!!! YAY!!! If the hare wins, display Hare wins. Yuch. 

If both animals win on the same tick of the clock, you may want to favor the tortoise (the
“underdog”), or you may want to display "It's a tie". If neither animal wins, perform
the loop again to simulate the next tick of the clock. When you’re ready to run your
application, assemble a group of fans to watch the race. You’ll be amazed at how involved
your audience gets!'''

def Tortoise_Hare():
    START_LINE = 1
    FINISH_LINE = 70
    TURN_DELAY_SEC = 1

    def tort_move():
        '''Return a randomized number of squares that represent the tortoise's move.'''
        import random as r
        i = r.randint(1,10)
        move = 0

        if i <= 5: 
            move = 3 #fast plod
        elif i <= 7: 
            move = -6 #slip
        else:
            move = 1 #slow plod

        return move
    
    def hare_move():
        '''Return a randomized number of squares that represent the hare's move.'''
        import random as r
        i = r.randint(1,10)
        move = 0

        if i <= 2: 
            move = 0 #sleep
        elif i <= 4: 
            move = 9 #big hop
        elif i <= 5: 
            move = -12 #big slip
        elif i <= 8: 
            move = 1 #small hop
        else:
            move = -2 #small slip
        
        return move

    def starting_gun():
        print('BANG !!!!!\nAND THEY\'RE OFF !!!!!')

    def run_race():
        import time
        t_pos = 1
        h_pos = 1
        race_on = True
        starting_gun()
        while race_on:
            time.sleep(TURN_DELAY_SEC / 10)

            t_pos += tort_move()
            h_pos += hare_move()
            
            if t_pos < 1:
                t_pos = 1
            if h_pos < 1:
                h_pos = 1

            progress_indicator = ''
            for p in range(START_LINE, FINISH_LINE + 1):
                if p == t_pos and p == h_pos:
                    progress_indicator += 'OUCH!!!'
                elif p == t_pos:
                    progress_indicator += 'T'
                elif p == h_pos:
                    progress_indicator += 'H'
                elif p == START_LINE or p == FINISH_LINE:
                    progress_indicator += '|'
                else:
                    progress_indicator += ' '

            # check for ending conditions
            if t_pos == FINISH_LINE and h_pos == FINISH_LINE:
                progress_indicator += '  It\'s a tie.'
                print(progress_indicator)
                race_on = False
            elif t_pos == FINISH_LINE:
                progress_indicator += '  TORTOISE WINS!!! YAY!!!'
                print(progress_indicator)
                race_on = False
            elif h_pos == FINISH_LINE: 
                progress_indicator += '  Hare wins. Yuch.'
                print(progress_indicator)
                race_on = False
            else:
                print(progress_indicator)

    run_race()

Tortoise_Hare()