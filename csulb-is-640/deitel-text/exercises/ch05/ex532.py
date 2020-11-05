'''
5.32 (Intro to Data Science: Rolling Two Dice) Modify the script RollDie.py that we
provided with this chapter’s examples to simulate rolling two dice. Calculate the sum of
the two values. Each die has a value from 1 to 6, so the sum of the values will vary from 2
to 12, with 7 being the most frequent sum, and 2 and 12 the least frequent. The following
diagram shows the 36 equally likely possible combinations of the two dice and their corresponding sums:

    1   2   3   4   5   6
1   2   3   4   5   6   7
2   3   4   5   6   7   8
3   4   5   6   7   8   9
4   5   6   7   8   9   10
5   6   7   8   9   10  11
6   7   8   9   10  11  12

If you roll the dice 36,000 times:
    • The values 2 and 12 each occur 1/36th (2.778%) of the time, so you should
    expect about 1000 of each.
    • The values 3 and 11 each occur 2/36ths (5.556%) of the time, so you should
    expect about 2000 of each, and so on.

Use a command-line argument to obtain the number of rolls. Display a bar plot summarizing the roll 
frequencies. The following screen captures show the final bar plots for sample executions of 360, 
36,000 and 36,000,000 rolls. Use the Seaborn barplot function’s optional orient keyword argument to 
specify a horizontal bar plot.
'''

def show_freq_distribution(chart_title='Frequency Distribution', axis_lbl = '', data=[], data_labels=True, vertical=True):
    '''
    Displays a bar chart representing the frequency distribution of the unique values of a given List object.

            Parameters:
                    chart_title (str): a string representing the chart title
                    axis_lbl (str): a string representing the axis label for the dependent variable 
                    data (List): a list containing the datapoints to be charted 
                    data_labels (bool): a boolean value indicating whether to display the frequency value and percentage over each bar 

            Returns:
                    None
    '''
    import matplotlib.pyplot as plt # why so slow? https://stackoverflow.com/questions/8955869/why-is-plotting-with-matplotlib-so-slow
    import seaborn as sns
    import numpy as np
    
    this_data = data
    this_y_label = 'Frequency'

    vals, freq = np.unique(this_data, return_counts=True)
    sns.set_style('whitegrid')

    this_orient = ''
    if vertical:
        this_orient = 'v'
    else:
        this_orient = 'h'
    
    axes = sns.barplot(x=vals, y=freq, palette='bright', orient=this_orient)
    title = chart_title
    x_label = axis_lbl
    y_label = this_y_label

    axes.set_title(title)
    axes.set(xlabel=x_label, ylabel=y_label)
    axes.set_ylim(top=max(freq) * 1.10)

    for bar, freq in zip(axes.patches, freq):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = ''
        if data_labels:
            text = f'{freq:,}\n{freq / len(this_data):.3%}'
        axes.text(text_x, text_y, text, fontsize=9, ha='center', va='bottom')

    plt.show()

def roll_dice(roll_count=1, die_count=1, die_sides=20):
    '''
    Returns a list of random dice roll results as well as a string description of the rolls that were executed.

            Parameters:
                    roll_count (int): an integer representing how many rolls to execute
                    die_count (int): an integer representing how many dice to use for each roll 
                    die_sides (int): an integer representing the number of sides on each die

            Returns:
                    result (List): a List containing the random roll results
                    summary (str): the natural language description of the rolls that were executed.  
    '''
    import random

    ROLL_COUNT = roll_count
    DIE_SIDES = die_sides
    DIE_COUNT = die_count

    results = [[random.randrange(1, DIE_SIDES + 1) for i in range(ROLL_COUNT)] for j in range(DIE_COUNT)]
    result = [sum(x) for x in zip(*results)]

    die_word = 'Die'
    if DIE_COUNT > 1:
        die_word = 'Dice'
    roll_summary = f'Rolling {DIE_COUNT} {DIE_SIDES}-Sided {die_word} {ROLL_COUNT:,} Times'

    return result, roll_summary

def analyse_dice_rolls(rolls=1, dice=1, sides=6, tests=1):
    base_rolls = rolls
    this_dice = dice
    this_sides = sides
    dependent_variable = 'Roll Values'
    this_tests = tests

    for i in range(1, this_tests + 1):
        this_roll_count = base_rolls * 10**i
        rolls, summary = roll_dice(this_roll_count, this_dice, this_sides)
        show_freq_distribution(summary, dependent_variable, rolls)

BASE_ROLL_COUNT = 36
DIE_SIDES = 6
DIE_COUNT = 2
TESTS = 3
analyse_dice_rolls(BASE_ROLL_COUNT, DIE_COUNT, DIE_SIDES, TESTS)