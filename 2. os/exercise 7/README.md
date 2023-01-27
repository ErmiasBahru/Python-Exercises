# Exercise 7

Using the built-in os module create a directory called `images`. Then create two directories in this directory named `images_png` and `images_jpg`. Before creating each directory, check if such directory exists.

```python exercise.py
import os

base_dir = 'images'

# add your solution here

for root, dirs, files in os.walk(base_dir):
    print(root)

```

## Expected result

```cmd
images
images/images_jpg
images/images_png
```
