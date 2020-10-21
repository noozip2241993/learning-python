'''
5.20 [Display a Two-Dimensional List in Tabular Format] Define a function named
display_table that receives a two-dimensional list and displays its contents in tabular format. List the column indices as headings across the top, and list the row indices at the left
of each row.
'''

names = [['First Name', 'Last Name'], ['Noel', 'Schieber'],
['Danyelle', 'Scranton'],
['Dori', 'Marone'],
['Ernie', 'Guido'],
['Ulysses', 'Jones'],
['Barbie', 'Aune'],
['Ines', 'Wilkens'],
['Bradley', 'Raub'],
['Maia', 'Barboza'],
['Daphne', 'Jamal'],
['Merlin', 'Albano'],
['Janeen', 'Heard'],
['Dillon', 'Jones'],
['Theressa', 'Siddiqui'],
['Lucila', 'Stahly'],
['Chara', 'Battista'],
['Martina', 'Mckibben'],
['Suzanna', 'Allman'],
['Mariette', 'Pelosi'],
['Karleen', 'Piel'],
['Alaina', 'Capers'],
['Eleanore', 'Flannigan'],
['Drucilla', 'Rudnicki'],
['Idalia', 'Bridgers'],
['Dolly', 'Tipler'],
['Margarito', 'Jones'],
['Junie', 'Schreffler'],
['Li', 'Shellhammer'],
['Myron', 'Pound'],
['Bev', 'Archer'],
['Amal', 'Oldham'],
['Ardell', 'Cantley'],
['Dede', 'Hastie'],
['Sherika', 'Jones'],
['Amira', 'Veatch'],
['Bobette', 'Nokes'],
['Olinda', 'Dipiazza'],
['Norman', 'Prock'],
['Toccara', 'Pohlmann'],
['Vinnie', 'Gunnells'],
['Letha', 'Baggs'],
['Carlyn', 'Kring'],
['Jesusita', 'Rasmusson'],
['Suzanne', 'Giebler'],
['Edna', 'Jones'],
['Ruth', 'Feggins'],
['Siu', 'Morganti'],
['Debby', 'Schlabach'],
['Emily', 'Williamson'],
['Vonda', 'Jones']]

def display_table(two_dim_list=[[]]):
    in_list = two_dim_list

    col_0_values = [x for x in range(len(in_list))]
    col_1_values = [(x[0]) for x in in_list]
    col_2_values = [(x[1]) for x in in_list]

    print(col_0_values)
    print(col_1_values)
    print(col_2_values)
    pass

display_table(names)