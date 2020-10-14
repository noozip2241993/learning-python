print("5.5 (IPython Session: Slicing)\n\
Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz', \n\
then perform the following separate slice operations to obtain:\n")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
middle = int(len(alphabet) / 2)
end = len(alphabet)

print("a) The first half of the string using starting and ending indices.")
print('   ' + alphabet[0:middle] + '\n')
print("b) The first half of the string using only the ending index.")
print('   ' + alphabet[:middle] + '\n')
print("c) The second half of the string using starting and ending indices.")
print('   ' + alphabet[middle:end] + '\n')
print("d) The second half of the string using only the starting index.")
print('   ' + alphabet[middle:] + '\n')
print("e) Every second letter in the string starting with 'a'.")
print('   ' + alphabet[::2] + '\n')
print("f) The entire string in reverse.")
print('   ' + alphabet[::-1] + '\n')
print("g) Every third letter of the string in reverse starting with 'z'.")
print('   ' + alphabet[::-3] + '\n')