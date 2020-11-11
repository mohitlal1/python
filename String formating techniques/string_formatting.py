# String formatting
from string import Template

name = 'John Snow'
question = 'how many'

print('Hello, %s' % name)

print('Hello, {}'.format(name))

def greet(name, question):
	print(f"Hello, {name}! Are you watching {question}?")

greet('Arya', 'Game of Thrones')

templ_string = 'Hey $name, $question next episodes are coming???'

print(Template(templ_string).substitute(name = name, question = question))