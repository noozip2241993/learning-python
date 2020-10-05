
# discrete probability statistics and common methods

def mean_discrete_prob_dist(prob_dist):
    '''
    Given a list of tuples that represent the possible outcomes and their 
    cooresponding likelihood (a discrete probability distribution). 
    Calculate the mean of each value. By multiplying each outcome by it's
    likelihood then add these products and divide by the number of 
    possible outcomes.
    '''
    mean = 0
    for row in prob_dist:
        mean += row[0] * row[1]
    mean /= len(prob_dist)
    return mean

def variance_discrete_prob_dist(prob_dist):
    '''
    Given a list of tuples that represent the possible outcomes and their 
    cooresponding likelihood of a discrete probability distribution.
    Calculate the varaince of discrete probability distribution
    1. subtract the mean from each value and square the difference
    2. multiply the squared difference by it's probability
    3. sum the resulting products
    '''
    mean = mean_discrete_prob_dist(prob_dist)
    variance = 0
    for row in prob_dist:
        variance += ((row[0] - mean)**2) * row[1]
    return variance

def display_table_discrete_prob_dist(list_of_tuples, random_variable_name):
    '''
    How to call:
    emergency_call_data = [(0,8),(1,10),(2,22),(3,9),(4,1)]
    display_table_discrete_prob_dist(emergency_call_data, 'Calls')
    '''
    prob_dist = []

    # calc the total frequency, mean
    total_frequency = 0
    mean = 0
    for element in list_of_tuples:
        total_frequency += element[1]
        mean += element[0] * element[1]
    mean = mean / total_frequency

    #construct the probability distribution
    variance_sum = 0
    for element in list_of_tuples:
        x = element[0]
        frequency = element[1]
        probability = frequency / total_frequency
        xpx = x * probability
        variance = ((mean - x)**2) * probability
        variance_sum += variance
        prob_dist.append([x, frequency, probability, xpx, variance])
    std_dev = variance_sum**(1/2)

    #display the probability distribution
    print(f'{random_variable_name + " (x)":<10}{"Frequency":<10}{"P(x)":<10}{"x*P(x)":<10}{"(x-u)^2*P(x)":<10}')
    for element in prob_dist:
        print(f'{element[0]:<10}{element[1]:<10}{element[2]:<10.2f}{element[3]:<10.2f}{element[4]:<10.4f}')
    print(f'{"":<10}{total_frequency:<10}{"":<10}{mean:<10.2f}{variance_sum:<10.4f}')

    return prob_dist

def cumulative_discrete_prob_gt_x(x, prob_dist):
    cumul_prob = 0
    for element in prob_dist:
        if element[0] >= 3:
            cumul_prob += element[2]
    return cumul_prob


# Usage examples
emergency_call_data = [(0,8),(1,10),(2,22),(3,9),(4,1)]
prob_dist = display_table_discrete_prob_dist(emergency_call_data, 'Calls')
print(f'The mean of emergency calls per day is {mean_discrete_prob_dist(prob_dist):.4f}')
print(f'The variance of emergency calls per day is {variance_discrete_prob_dist(prob_dist):.4f}')
x = 3
print(f'The probability that {x} or more calls will come occur in a day is {cumulative_discrete_prob_gt_x(x, prob_dist):.4f}')