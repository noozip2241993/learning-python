direction = "5.3 (Fill in the Missing Code) \n\
Replace the ***s in the following list comprehension and map function call, such that given \n\
a list of heights in inches, the code maps the list to a list of tuples containing the original \n\
height values and their corresponding values in meters. For example, if one element in the original \n\
list contains the height 69 inches, the corresponding element in the new list will contain the tuple \n\
(69, 1.7526), representing both the height in inches and the height in meters. \n\
There are 0.0254 meters per inch.\n\
[*** for x in [69, 77, 54]] \n\
list(map(lambda ***, [69, 77, 54]))"

heights = [x for x in [69, 77, 54]]
print(list(map(lambda x: (x, x * 0.0254), heights)))