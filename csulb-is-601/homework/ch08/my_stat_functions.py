

def std_error_of_mean(pop_std_deviation, observations):
    import math
    return pop_std_deviation / math.sqrt(observations)

def z_value_known_sigma(sample_mean, population_mean, population_std_dev, observations):
    import math
    return (sample_mean - population_mean) / (population_std_dev / math.sqrt(observations))

#def area_under_norm_dist(z_value):
    #Write a fuction to lookup a z-value against the table B.3 Areas under the Normal Curve