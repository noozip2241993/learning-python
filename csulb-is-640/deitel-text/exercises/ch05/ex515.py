'''
5.15 (Tuples Representing Invoices) When you purchase products or services from a
company, you typically receive an invoice listing what you purchased and the total amount
of money due. Use tuples to represent hardware store invoices that consist of four pieces
of data—a part ID string, a part description string, an integer quantity of the item being
purchased and, for simplicity, a float item price (in general, Decimal should be used for
monetary amounts). Use the sample hardware data shown in the following table.

Part number Part description    Quantity    Price
83          Electric sander     7           57.98
24          Power saw           18          99.99
7           Sledge hammer       11          21.50
77          Hammer              76          11.99
39          Jig saw             3           79.50

Perform the following tasks on a list of invoice tuples:
    a) Use function sorted with a key argument to sort the tuples by part description,
    then display the results. To specify the element of the tuple that should be used
    for sorting, first import the itemgetter function from the operator module as in
    from operator import itemgetter
    Then, for sorted’s key argument specify itemgetter(index) where index
    specifies which element of the tuple should be used for sorting purposes.
    b) Use the sorted function with a key argument to sort the tuples by price, then
    display the results.
    c) Map each invoice tuple to a tuple containing the part description and quantity,
    sort the results by quantity, then display the results.
    d) Map each invoice tuple to a tuple containing the part description and the value
    of the invoice (the product of the quantity and the item price), sort the results
    by the invoice value, then display the results.
    e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.
    f) Calculate the total of all the invoices
'''
# Create the invoice variables and put them on a list
invoices = []
invoices.append((83, 'Electric sander', 7, 57.98))
invoices.append((24, 'Power saw', 18, 99.99))
invoices.append((7, 'Sledge hammer', 11, 21.50))
invoices.append((77, 'Hammer', 76, 11.99))
invoices.append((39, 'Jig saw', 3, 79.50))

# a) Use function sorted with a key argument to sort the tuples by part description,
# then display the results. To specify the element of the tuple that should be used
# for sorting, first import the itemgetter function from the operator module as in
# from operator import itemgetter
from operator import itemgetter
print('via itemgetter')
print(sorted(invoices, key=itemgetter(1))) # prefer to use lambdas for practice

print('via lambda')
print(sorted(invoices, key=lambda item: item[1]))

# b) Use the sorted function with a key argument to sort the tuples by price, 
# then display the results.
print(sorted(invoices, key=lambda item: item[3]))

# c) Map each invoice tuple to a tuple containing the part description and quantity, 
# sort the results by quantity, then display the results.
c = lambda tool: (tool[1], tool[2])
part_desc_by_qty = [c(item) for item in invoices]
print(sorted(part_desc_by_qty, key=lambda item: item[1]))

# d) Map each invoice tuple to a tuple containing the part description and the value 
# of the invoice (the product of the quantity and the item price), sort the results by 
# the invoice value, then display the results.
d = lambda tool: (tool[1], round(tool[2] * tool[3], 2))
part_desc_by_invoice_value = [d(item) for item in invoices]
print(sorted(part_desc_by_invoice_value, key=lambda item: item[1]))

# e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.
min = 200
max = 500
e = lambda tool: tool[1] >= min and tool[1] <= max
part_desc_by_invoice_value_in_range = filter(e, part_desc_by_invoice_value)
print(sorted(part_desc_by_invoice_value_in_range, key=lambda item: item[1]))

# f) Calculate the total of all the invoices
# Using a generator expression
total = sum(float(value) for desc, value in part_desc_by_invoice_value)
print(total)