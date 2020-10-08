import math

#def area_under_norm_dist(z_value):
    #Write a fuction to lookup a z-value against the table B.3 Areas under the Normal Curve

def sample_mean(sample=()):
    mean = 0
    for obs in sample:
        mean += obs
    mean /= len(sample)
    return mean

def sample_variance(sample=()):
    mean = sample_mean(sample)
    sum_squares = 0
    for obs in sample:
        sum_squares += (obs - mean)**2
    result = sum_squares / (len(sample) - 1)
    return result

def sample_std_dev(sample=()):
    return math.sqrt(sample_variance(sample))

#CHAPTER 8
def std_error_of_mean(pop_std_deviation, observations, verbose=False):
    result = pop_std_deviation / math.sqrt(observations)
    print (f'{result:.4f}')
    return result

def z_value_known_sigma(sample_mean, population_mean, population_std_dev, observations, verbose=False):
    result = (sample_mean - population_mean) / (population_std_dev / math.sqrt(observations))
    print (f'{result:.3f}')
    return result

#CHAPTER 9
def confidence_interval(sample_mean, population_std_dev, observations, z_value=1.96, verbose=False):
    error = margin_error(population_std_dev, observations, z_value, False)
    result = (sample_mean - error, sample_mean + error)
    if verbose:
        print(f'{result[0]:.3f}, {result[1]:.3f}')
    return result

def margin_error(sample_std_dev, observations, z_value, verbose=False):
    result = z_value * (sample_std_dev / math.sqrt(observations))
    if verbose:
        print(f'{result:.3f}')
    return result

def confidence_interval_no_sigma(sample_mean, sample_std_dev, observations, t_value, verbose=False):
    margin_error = margin_error_no_sigma(sample_std_dev, observations, t_value, False)
    result = (sample_mean - margin_error, sample_mean + margin_error)
    if verbose:
        print(f'{result[0]:.3f}, {result[1]:.3f}')
    return result

def margin_error_no_sigma(sample_std_dev, observations, t_value, verbose=False):
    result = t_value * (sample_std_dev / math.sqrt(observations))
    if verbose:
        print(f'{result:.3f}')
    return result

def confidence_interval_pop_proportion(sample_proportion, observations, z_value, verbose=False):
    p = sample_proportion
    n = observations
    z = z_value
    margin_err = z * math.sqrt((p * (1 - p)) / n)
    low = p - margin_err
    high = p + margin_err
    result = (low, high)
    if verbose:
        print(f'{result[0]:.4f}, {result[1]:.4f}')
    return result

def margin_error_pop_proportion(sample_proportion, observations, t_value, verbose=False):
    p = sample_proportion
    n = observations
    t = t_value
    margin_err = t * math.sqrt((p * (1 - p)) / n)
    if verbose:
        print(f'{margin_err:.4f}')
    return margin_err

def sample_size_population_proportion(max_allowable_error, z_value, population_proportion, verbose=False):
    pi = population_proportion
    z = z_value
    E = max_allowable_error
    a = pi
    b = 1 - pi
    c = (z / E)**2
    sample_size = a * b * c
    sample_size = math.ceil(sample_size)
    if verbose:
        print(f'{sample_size:.0f}')
    return sample_size

def sample_size_population_mean(z_value, max_allowed_error, pop_std_deviation, verbose=False):
    z = z_value
    sigma = pop_std_deviation
    E = max_allowed_error
    a = z * sigma
    sample_size = ( a / E)**2
    sample_size = math.ceil(sample_size)
    if verbose:
        print(f'{sample_size:.0f}')
    return sample_size 