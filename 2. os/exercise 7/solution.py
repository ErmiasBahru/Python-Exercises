import os

base_dir = 'images'

# add your solution here

png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

if not os.path.exists(png_dir):
    os.mkdir(png_dir)

if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

for root, dirs, files in os.walk(base_dir):
    print(root)
