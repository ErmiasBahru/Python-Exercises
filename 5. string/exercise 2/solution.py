from string import Template
 
 
names = ['John', 'Paul', 'Lisa', 'Michael']
 
email = """Hello $name,
 
Thank you for visiting our website.
Team, XYZ"""

template = Template(email)

for name in names:
    print(template.substitute(name=name))
    print('-' * 35)