import re

text = 'Python 3.9'

print(re.findall(pattern=r'\D', string=text))
