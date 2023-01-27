import os

names = sorted([name for name in os.listdir() if name.startswith('e')])

print(names)
