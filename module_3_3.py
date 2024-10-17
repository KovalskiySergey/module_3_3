def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

value_list = ['Urban', False, 13]
value_list_2 = [12, 'Sergey']
value_dict = {'a' : True, 'b' : 'URBAN', 'c' : 12}
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)