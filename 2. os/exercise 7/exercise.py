import os


base_dir = 'images'

# add your solution here

for root, dirs, files in os.walk(base_dir):
    print(root)
