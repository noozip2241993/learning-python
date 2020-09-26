'''
Write a script that computes the value of π from the following infinite series. 
Print a table that shows the value of π approximated by one term of this series, 
by two terms, by three terms, and so on. How many terms of this series do you 
have to use before you first get 3.14? 3.141? 3.1415? 3.14159?
'''

#initialization
TOT_TERMS = 1000000
NUMERATOR = 4
denom = -3
pi = 4 #term 1
terms = 1

#processing
while terms < TOT_TERMS:
   pi += (NUMERATOR / denom) #add the next term
   denom *= -1 # switch the sign for the next term
   if denom < 0: #iterate the demoninator by two in the direction of the next term
       denom -= 2 
   else:
       denom += 2
   terms += 1 #add 1 to the term counter

#termination
print(f'With {TOT_TERMS} terms pi = {pi}')
