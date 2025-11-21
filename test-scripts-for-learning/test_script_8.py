# String Error (was --> print('Hello, world!) )
print('Hello, world!')
      
# Indentation Error (was --> print line unindented)
if True:
    print('Ahoy, matey!')
      
# Syntax Error (was --> no : after True)
if True:
    print('Greetings, Earthlings!')

# Logic Error (was --> if animal == 'Lino')
animal = 'Lion'
if animal == 'Lion':
    print('Meat')
elif animal == 'Zebra':
    print('Grass')
else:
    print('Water')