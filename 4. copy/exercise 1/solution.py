import copy

carts = [['Apple', '1KG'], ['Milk'], ['2L']]
carts_copied = copy.copy(carts)

carts[0][0] = 'Banana'

print(f'carts: {carts}')
print(f'carts_copied: {carts_copied}')
