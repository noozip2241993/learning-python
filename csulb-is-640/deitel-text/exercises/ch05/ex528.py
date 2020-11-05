'''
5.28 (Intro to Data Science: Survey Response Statistics) Twenty students were asked to
rate on a scale of 1 to 5 the quality of the food in the student cafeteria, with 1 being “awful”
and 5 being “excellent.” Place the 20 responses in a list

    1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5

Determine and display the frequency of each rating. Use the built-in functions, statistics module 
functions and NumPy functions demonstrated in Section 5.17.2 to display the following response 
statistics: minimum, maximum, range, mean, median, mode, variance and standard deviation.
'''
FOOD_RATINGS = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

def descriptive_stats_numpy(numberical_data=[], verbose=False):
    import statistics as stats
    import numpy as np
    
    in_data = numberical_data
    this_min = np.min(in_data)
    this_max = np.max(in_data)
    this_range = this_max - this_min + 1
    this_mean = np.mean(in_data)
    this_median = np.median(in_data)
    this_mode = stats.mode(in_data)
    this_variance = np.var(in_data)
    this_std_dev = np.std(in_data)

    result = []
    result.append(('Minimum', this_min))
    result.append(('Maximum', this_max))
    result.append(('Range', this_range))
    result.append(('Mean', this_mean))
    result.append(('Median', this_median))
    result.append(('Mode', this_mode))
    result.append(('Variance', this_variance))
    result.append(('Standard Deviation', this_std_dev))

    if verbose:
        print('Descriptive Stats via numpy module')
        [print(f'{row[0]:>20} {row[1]:.4f}') for row in result]
        print()
    
    return result

def descriptive_stats_stats_module(numberical_data=[], verbose=False):
    import statistics as stats
    
    in_data = numberical_data

    this_min = min(in_data)
    this_max = max(in_data)
    this_range = this_max - this_min + 1
    this_mean = stats.mean(in_data)
    this_median = stats.median(in_data)
    this_mode = stats.mode(in_data)
    this_variance = stats.variance(in_data)
    this_std_dev = stats.stdev(in_data)

    result = []
    result.append(('Minimum', this_min))
    result.append(('Maximum', this_max))
    result.append(('Range', this_range))
    result.append(('Mean', this_mean))
    result.append(('Median', this_median))
    result.append(('Mode', this_mode))
    result.append(('Variance', this_variance))
    result.append(('Standard Deviation', this_std_dev))

    if verbose:
        print('Descriptive Stats via via the statistics module and built-in functions')
        [print(f'{row[0]:>20} {row[1]:.4f}') for row in result]
        print()
    
    return result

descriptive_stats_stats_module(FOOD_RATINGS, verbose=True)
descriptive_stats_numpy(FOOD_RATINGS, verbose=True)

pass
