my_dict = {'name':'jack','age':'26'}

print(my_dict['name'])
print(my_dict.get('age'))

# doesnt acess keys which
# doesnt access throws error
#  print(my_dict['address'])

# update value
my_dict['age'] = 27
print(my_dict)

# add item

my_dict['address']= 'downtown'
print(my_dict)

# remove element from dictionary

squares = {1: 1,2: 4,3: 9,4: 16,5: 25}
print(squares.pop(4))

# remove an arbitary element item ,return
print(squares.popitem())

# clear function
print(squares.clear())
