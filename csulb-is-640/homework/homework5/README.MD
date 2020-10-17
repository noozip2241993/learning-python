# Homework 5

Due: 10/30 at 11:59pm.  Please do it early because you need a working development environment for the following study.

Please read https://github.com/ying-teaching/python/blob/master/0-installation-setup/git-and-github.md for detail instructions to setup your development tools, create a Github account, and  how to push your code to GitHub repository.
## 1.	The Submission
The detail requirements are given in the next section. Once you complete it, please create a one-line text file (a file with “.txt” postfix) that a link to your GitHub homework repository. It is recommended to use a repository name that is the same as your homework.  Please submit the text file to the BeachBoard dropbox.  

For example, below is the sample content of your hw.txt (the link is a sample link, please change it to your GitHub repository) for homeworkx (x is the homework number such as 1, 2 ,3…)

https://github.com/your-github-name/homeworkx.git

Wrong file format, invalid URL, or un-working file is in-completed and gets 0 point. 

## 2.	The Tasks

Create a folder “homework5” as your project workspace. It is the root folder of your homework project. It has two files for the following two tasks.

### 2.1	“task1.py” file

Assume that a file containing a series of student scores is named “scores.txt”.  It may have the following content:

Alice 69
Bob  89
Cindy 79


Write a program that calculates the number of students and the average of all the scores stored in the file and print the output: 

The class average is 79 for 3 students.

Also write the output to a log.txt file. You should use the with

It should handle IOError exceptions that are raised when it fails to open the file, display an error message with the detail error exception and stop. For example, it happens when there is no scores.txt in the current folder.

For the following content, it should handle any ValueError exceptions that are raised when the items
that are read from the score field are failed to be converted to a number by printing an error message and skip the record.  There could be multiple error values to be ignored. For example, the data could be:

Alice 69
Bob eight-seven
Cindy 79
David 89
Eric abc

For the above data, it should skip both Bob and Eric and display:

Bad score value for Boy, ignored.
Bad score value for Eric, ignored.
The class average is 79 for 3 students.

The log.txt file should have the same content as the above output.

### 2.2	“task2.py” file 

Read a text file named “book.txt” that may have multiple lines. Then create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter. Each line has a record of the letter and frequency. The last line should be a summary to tell if the file has all 26 letters. A sample “summary.txt” is:

A 25
C 36
…
X 2
Z 4

It doesn’t have all letters.

Another “book.txt” may generate the “summary.txt” as the following:

A 25
B 36
…
X 2
Y 1
Z 4

It has all letters.

