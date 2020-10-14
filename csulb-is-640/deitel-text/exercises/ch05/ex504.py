print("5.4 (Iteration Order) Create a 2-by-3 list, then use a nested loop to:\n\
a) Set each element’s value to an integer indicating the order in which it was\n\
processed by the nested loop.\n\
b) Display the elements in tabular format. Use the column indices as headings\n\
across the top, and the row indices to the left of each row.")

my_list =  [[1, 2, 3],
            [4, 5, 6]]
processed = 0
this_row = 0

head = '  '
for i in enumerate(my_list[0]):
    head += str(i[0])
print(head)

for i, row in enumerate(my_list):
    print(f'{this_row} ', end='')
    this_col = 0

    for j, item in enumerate(row):
        item = processed 
        print(item, end='')
        processed += 1
        this_col += 1
    
    print()
    this_row += 1