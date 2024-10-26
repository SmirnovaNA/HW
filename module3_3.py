def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('Наташа', 1990,)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['Химия', 46, False]
values_dict = {'a': 1990, 'b': 'Nata', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Химия', 46]
print_params(*values_list_2, 42)
