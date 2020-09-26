'''The great British mathematician Alan Turing proposed a simple test to determine whether 
machines could exhibit intelligent behavior. A user sits at a computer and does the same 
text chat with a human sitting at a computer and a computer operating by itself. The user 
doesn’t know if the responses are coming back from the human or the independent computer. 
If the user can’t distinguish which responses are coming from the human and which are coming 
from the computer, then it’s reasonable to say that the computer is exhibiting intelligence.

Create a script that plays the part of the independent computer, giving its user a simple 
medical diagnosis. The script should prompt the user with 'What is your problem?' When the 
user answers and presses Enter, the script should simply ignore the user’s input, then prompt 
the user again with 'Have you had this problem before (yes or no)?' If the user enters 'yes', 
print 'Well, you have it again.' If the user answers 'no', print 'Well, you have it now.'''

prompt1 = 'What is your problem?'
prompt2 = 'Have you had this problem before (yes or no)?'
prompt3 = 'Well, you have it'
prompt4 = "I'm sorry you're having trouble, let's try again."
problem_solved = False

while problem_solved != True:
    reply = input(prompt1)
    print(prompt1, reply)
    reply = input(prompt2)
    print(prompt2, reply)
    if (reply == 'yes'):
        print(prompt3, 'again.')
        problem_solved = True
    elif (reply == 'no'):
        print(prompt3, 'now.')
        problem_solved = True
    else:
        print(prompt4)
        problem_solved = False

print('Smell ya later clown.')

'''Would this conversation convince the user that the entity at the other end exhibited 
intelligent behavior? Why or why not?

No, a few clues are that the prompts don't ever vary slightly and the advice provided is 
never specific. There is also no delay in response indicating no human on the other end.'''