import string

docs = 'programming in python'
code_map = dict((enumerate(string.ascii_lowercase)))
code_map_inv = {val: key for key, val in code_map.items()}

result = ''
for char in docs:
    if char == ' ':
        result += ' '
        continue
    idx = (code_map_inv[char] + 3) % 26
    result += code_map[idx]

print(result)
