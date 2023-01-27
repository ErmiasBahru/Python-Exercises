import os

os.mkdir('sales')

dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]

for name in dirnames:
    path = os.path.join('sales', name)
    os.mkdir(path)
    
print(sorted(os.listdir('sales')))
