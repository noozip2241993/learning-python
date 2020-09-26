'''
Write a script that estimates the value of the mathematical constant e by using the formula below. Your script
can stop after summing 10 terms.

e = 2.71828182845904523536028747135266249775724709369995
'''

#initialization
TOT_TERMS = 10
NUMERATOR = 1
denom = 1
e = 1 #term 1
terms = 1

#processing
while terms < TOT_TERMS:
    denom *= terms
    e += (NUMERATOR / denom) #add the next term
    terms += 1 #add 1 to the term counter

#termination
print(f'With {TOT_TERMS} terms e = {e}')