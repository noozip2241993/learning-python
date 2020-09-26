# Chapter 04 Non-Coding Exercises
## Exercise 401
**(Discussion: else Clause) In the script of Fig. 4.1, we did not include an else clause in the if…elif statement. What are the possible consequences of this choice?**
*In theory the 'face' variable could be assigned an unexpected value, which is not accounted for in the if and elif statements. If that happens that value would not be counted in our outputted frequency table*

## Exercise 402
**(Discussion: Function-Call Stack) What happens if you keep pushing onto a stack, without enough popping?**
*Eventually the system will reach it's memory limitations and a Stack-Overflow Error will occur.*

## Exercise 403
**(What’s Wrong with This Code?) What is wrong with the following cube function’s definition?**

    def cube(x):
        """Calculate the cube of x."""
        x ** 3
    print('The cube of 2 is', cube(2))

*No matter what the value is for the argument x, the output will read 'The cube of ***2*** is' followed by the correct cube value of the argument value.*

## Exercise 404
**(What’s Does This Code Do?) What does the following mystery function do? Assume you pass the list [1, 2, 3, 4, 5] as an argument.**

    def mystery(x):
        y = 0
        for value in x:
            y += value ** 2
        return y

*The mystery function sums the squares of the argumeents padded to it. Passing the list [1, 2, 3, 4, 5] as an argument will result in a return value for y = 1 + 4 + 9 + 16 + 25 = 55*

## Exercise 418
**(Functional-Style Programming: Internal vs. External Iteration) Why is internal iteration preferable to external iteration in functional-style programming?**

*Internal iteration hides the how of interation from the user which reduces the degree of complexity and opportunities for errors*

## Exercise 419 
**(Functional-Style Programming: What vs. How) Why is programming that emphasizes “what” preferable to programming that emphasizes “how”? What is it that makes “what” programming feasible?**

*Functional-style programing emphasizes 'what' and is preferable because it reduces the compexity presented to the user and in turn presents less opportunity for error-prone coding. The existence of defined functions makes 'what' programming feasable because the 'how' can be safely tucked away in a function out of the hands of the user. This ensures that the how is executed in a consistent and predictable way every time.*

## Exercise 420
**(Intro to Data Science: Population Variance vs. Sample Variance) We mentioned in the Intro to Data Science section that there’s a slight difference between the way the statistics module’s functions calculate the population variance and the sample variance. The same is true for the population standard deviation and the sample standard deviation. Research the reason for these differences.**

***From Wikipedia***
> In statistics, Bessel's correction is the use of 'n − 1' instead of 'n' in the formula for the sample variance and sample standard deviation, where 'n' is the number of observations in a sample. This method corrects the bias in the estimation of the population variance. It also partially corrects the bias in the estimation of the population standard deviation. However, the correction often increases the mean squared error in these estimations.[1]

*So 'n - 1' is used in the calculation of sample variance and std deviation in order to correct for bias in those formulas.*

*The sample mean will always sit within the sample range. Depending on the data points in the sample, it is possible that the true Population mean could not sit within the sample range. Because of this the biased sample variance (where the denominator is 'n' not 'n - 1') will always be an underestimation of the population mean. By instead using a denominator of 'n - 1' (smaller than 'n') we will get a larger sample variance.*[2]

***But why 'n - 1' and not 'n - 2'?***

*By observing the statistics of possible samples within a given population we can find that the biased sample variance does not approach the population variance as the sample size (n) gets larger. Instead it approaches (n-1)(pop_variance) / n. For example:*

    When n = 2 the biased sample tends to be (2-1)(pop_variance) / 2 = 1/2(pop_variance) = 50% * pop_variance
    When n = 3 the biased sample tends to be (3-1)(pop_variance) / 3 = 2/3(pop_variance) = 67% * pop_variance
    When n = 4 the biased sample tends to be (4-1)(pop_variance) / 4 = 3/4(pop_variance) = 75% * pop_variance
    ...
    When n = n the biased sample tends to be (n-1)(pop_variance) / n

*From there algebra tells us that:*[3]

    bias_sample_variance = sum((x - x_bar)**2) / n = (n-1)(pop_variance) / n
    (n / n-1)(sum((x - x_bar)**2) / n ) = (n / n-1)(n-1)(pop_variance) / n
    (sum((x - x_bar)**2) / n-1 ) = (pop_variance)

[1]: https://en.wikipedia.org/wiki/Bessel%27s_correction "Bessels correction"

[2]: https://www.youtube.com/watch?v=KkaU2ur3Ymw "Review and intuition why we divide by n-1 for the unbiased sample | Khan Academy"

[3]: https://www.youtube.com/watch?v=Cn0skMJ2F3c "Simulation showing bias in sample variance | Probability and Statistics | Khan Academy"
