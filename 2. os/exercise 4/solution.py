import os

file_name = sorted([name for name in os.listdir() if name.endswith('.py')])

print(file_name)
