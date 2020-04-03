x = float (input('First nuber: '))
y = float (input('Second number: '))
operation = input('Operation: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Unsupported operation ...')

if result is not None:
    print('Result: ', result)

# elif   Статься о множественном ветвелении в Python   https://younglinux.info/python/elif.php

'''
elif   Статься о множественном ветвелении в Python   https://younglinux.info/python/elif.php

'''
