item = {
    'title': 'kitten food',
    'price': 12.50,
    'discount': .2,
}

cart = [
    {
        'title': 'kitten food',
        'price': 12.50,
        'discount': .2,
    },
    {
        'title': 'kitten food',
        'price': 12.50,
        'discount': .2,
    },
    {
        'title': 'kitten food',
        'price': 12.50,
        'discount': .2,
    },
    {
        'title': 'kitten food',
        'price': 12.50,
        'discount': .2,
    },
    {
        'title': 'pencil',
        'price': .10,
    }
]

total = 0
savings = 0
for item in cart:
    print('I want ', item['title'])
    print('The price is', item['price'], 'each')
    if 'discount' in item:
        print('The discount is', item['discount'] * 100, 'percent off')
        savings += item['price'] * item['discount']
        total += (item['price'] * (1 - item['discount']))
    else:
        total += item['price']
    print()

print('The total would be:', total)

# create a new dictionary
there = 'there'
dictionary = {'hello': 'world', 'hi': there}

# add key value pair to dictionary
key = 'foo'
value = 'bar'
dictionary[key] = value

# updating key value pair in dictionary
value = 'foobar'
dictionary[key] = value

# delete key value pair from dictionary
del dictionary['foo']

# loop through (iterate) the dictionary
for key in dictionary:
    value = dictionary[key]

# check if key in dictionary
if key in dictionary:
    pass

# find the value in the dictionary
found = False
for key in dictionary:
    value = dictionary[key]
    if value == 'there':
        found = True
if found:
    print('the value was found')
else:
    print('the value was not found')
