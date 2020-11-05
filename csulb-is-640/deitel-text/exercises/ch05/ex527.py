'''
5.27 (Intro to Data Science: Duplicate Elimination and Counting Frequencies) Use a
list comprehension to create a list of 50 random values in the range 1 through 10. Use
NumPy’s unique function to obtain the unique values and their frequencies. Display the
results.
'''
def roll_die(roll_count=50, die_size=10):
    import random
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    RANDO_COUNT = roll_count
    RANDO_MIN = 1
    RANDO_MAX = die_size

    randos = [random.randint(RANDO_MIN, RANDO_MAX) for x in range(RANDO_COUNT)]
    vals, freq = np.unique(randos, return_counts=True)

    title = f'Rolling a {RANDO_MAX:,}-sided Die {len(randos):,} Times'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=vals, y=freq, palette='bright')
    axes.set_title(title)
    axes.set (xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(freq) * 1.10)
    for bar, freq in zip(axes.patches, freq):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{freq:,}\n{freq / len(randos):.3%}'
        axes.text(text_x, text_y, text, fontsize=9, ha='center', va='bottom')

    plt.show()

roll_die()