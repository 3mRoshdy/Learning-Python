"""
Lambda functions: (Anonymous functions)
Syntax :
lambda arguments: expression
"""

# using filter() function
my_list = [1, 2, 3, 4, 5, 6]
even_list = list(filter(lambda x: x % 2 == 0, my_list))

print('even_list: ', even_list)

# using map() function
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

list_items_multiplied = list(map(lambda x: x * 2 , my_list))

print('list_items_multiplied: ', list_items_multiplied)
