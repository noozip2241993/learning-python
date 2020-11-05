'''
5.30 (Intro to Data Science: Removing the Text Above the Bars)
Modify the die-rolling simulation in Section 5.17.2 to omit 
displaying the frequencies and percentages above each bar. Try 
to minimize the number of lines of code.
'''
def show_freq_distribution(chart_title='Frequency Distribution', x_axis_lbl = 'x', data=[], data_labels=True):
    '''
    Displays a bar chart representing the frequency distribution of the unique values of a given List object.

            Parameters:
                    chart_title (str): a string representing the chart title
                    x_axis_lbl (str): a string representing the x-axis label 
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
    axes = sns.barplot(x=vals, y=freq, palette='bright')

    title = chart_title
    x_label = x_axis_lbl
    y_label = this_y_label

    axes.set_title(title)
    axes.set (xlabel=x_label, ylabel=y_label)
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
                    roll_summary (str): the natural language description of the rolls that were executed.  
    '''
    import random

    ROLL_COUNT = roll_count
    DIE_SIDES = die_sides
    DIE_COUNT = 1 #multiple dice not implemented yet

    result = [random.randrange(1, DIE_SIDES + 1) for i in range(ROLL_COUNT)]
    roll_summary = f'Rolling {DIE_COUNT} {DIE_SIDES}-Sided Die {ROLL_COUNT:,} Times...'
    return result, roll_summary

ROLL_COUNT = 6000
DIE_COUNT = 1
DIE_SIDES = 6

rolls, summary = roll_dice(ROLL_COUNT, DIE_COUNT, DIE_SIDES)
show_freq_distribution(summary, 'Die Value', rolls, data_labels=False)