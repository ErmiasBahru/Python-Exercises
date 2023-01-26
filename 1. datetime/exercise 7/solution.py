from datetime import datetime

date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2022'

dt1 = datetime.strptime(date_str_1, '%d %B %Y')
dt2 = datetime.strptime(date_str_2, '%d/%m/%Y')
dt3 = datetime.strptime(date_str_3, '%d-%m-%Y')

print(dt1)
print(dt2)
print(dt3)
