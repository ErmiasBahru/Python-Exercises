# Exercise 1

Using the built-in string module, create a dictionary that allows you to map indices from 0 to 25 to lowercase letters (ascii_lowercase) and assign it to the `code_map` variable:

```
{
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z',
}
```

Then replace the values ​​with keys in the `code_map` dictionary and assign to the `code_map_inv` variable:

```
{
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
}
```

A text document is given:

```python
docs = 'programming in python'
```

Using the `code_map` and `code_map_inv` dictionaries, encode the docs in such a way that each letter is shifted by three letters alphabetically (leave the spaces in the document unchanged).

print the encoded document to the console.

## Expected result

```cmd
surjudpplqj lq sbwkrq
```
