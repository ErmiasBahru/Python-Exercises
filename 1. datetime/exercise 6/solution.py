from datetime import datetime

dt1 = datetime(2022, 4, 20, 11, 30, 00)

print(dt1.strftime('%Y-%m-%d'))
print(dt1.strftime('%d-%m-%Y'))
print(dt1.strftime('%m-%Y'))
print(dt1.strftime('%B-%Y'))
print(dt1.strftime('%d %B, %Y'))
print(dt1.strftime('%Y-%m-%d %H:%M:%S'))
print(dt1.strftime('%m/%d/%y %H:%M:%S'))
print(dt1.strftime('%d(%a) %B %Y'))
