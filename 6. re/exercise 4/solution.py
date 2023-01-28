import re

code = '0010-000-423'

print(re.findall(pattern=r"[^-]+", string=code))
