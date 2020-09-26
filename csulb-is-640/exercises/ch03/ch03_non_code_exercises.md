# Chapter 03 Non-Coding Exercises
## Exercise 302
**What is wrong with the following code?**

    a = b = 7
    print('a =', a, '\nb =', b)

*it's unclear the following is more readable.*

    a = 7
    b = 7
    print('a =', a, '\nb =', b)

## Exercise 303
**What does the following program print?**

    for row in range(10):
        for column in range(10):
            print('<' if row % 2 == 1 else '>', end='')
        print()

*it prints ten lines each of which 10 characters long comprised only of '<' on odd numbered lines and '>' on even numbered lines*

## Exercise 323
**The file validate_indents.py in this chapter’s ch03 examples folder contains the following code with incorrect indentation:**

    grade = 93
    
    if grade >= 90:
        print('A')
      print('Great Job!')
       print('Take a break from studying')
**The Python Standard Library includes a code indentation validator module named tabnanny, which you can run as a script to check your code for proper indentation—this is one of many static code analysis tools. Execute the following command in the ch03 folder to see the results of analyzing validate_indents.py: python -m tabnanny validate_indents.py Suppose you accidentally aligned the second print statement under the i in the if keyword. What kind of error would that be? Would you expect tabnanny to flag that as an error?**

## Exercise 324
**The prospector tool runs several popular static code analysis tools to check your Python code for common errors and to help you improve your code. Check that you’ve installed prospector (see the Before You Begin section that follows the Preface). Run prospector on each of the scripts in this chapter. To do so, open the folder containing the scripts in a Terminal (macOS/ Linux), Command Prompt (Windows) or shell (Linux), then run the following command from that folder:**
    
    prospector --strictness veryhigh --doc-warnings

**Study the output to see the kinds of issues prospector locates in Python code. In general, run prospector on all new code you create.**

## Exercise 325
**Locate a Python open-source project on GitHub, download its source code and extract it into a folder on your system. Open that folder in a Terminal (macOS/Linux), Command Prompt (Windows) or shell (Linux), then run the following command from that folder:**

    prospector --strictness veryhigh --doc-warnings

**Study the output to see more of the kinds of issues prospector locates in Python code.**

## Exercise 329
**For an odd number of values, to get the median you simply arrange them in order and take the middle value.**

**For an even number, you average the two middle values.**

**What problem occurs if those two values are different?**

*The median is not a value that is actually in the data set*

## Exercise 330
**In statistics, outliers are values out of the ordinary and possibly way out of the ordinary. Sometimes, outliers are simply bad data. In the data science case studies, we’ll see that outliers can distort results. Which of the three measures of central tendency we discussed—mean, median and mode—is most affected by outliers? Why? Which of these measures are not affected or least affected? Why?**

*The mean is most affected by outliers because it reflects a measure that takes all data point values into account. The median is impacted as well but less so. Cases where the count of outliers skew to one side of the median more than the other, will change the median. The mode is least impacted as it would take multiple outliers of the same value to be reflected in the mode. It is very rare that a data point value would occur enough to be the mode of a data set and still be considered an outlier. However, I imagine it could be possible.*

## Exercise 331
**Mean, median and mode work well with numerical values.**

**You can use them in calculations and arrange them in meaningful order.**

**Categorical values are descriptive names like Boxer, Poodle, Collie, Beagle, Bulldog and Chihuahua. Normally, you don’t use these in calculations nor associate an order with them. Which if any of the descriptive statistics are appropriate for categorical data?**

*Measures of frequency like count and percent*