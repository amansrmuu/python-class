my_set = {1,2,3}
print(my_set)

# mixed datatype

my_set = {1.0,'oye',(1,2,3)}
print(my_set)

# we cant make set from list

my_set = set([1,2,3,2])
print(my_set)

# set cant have duplicates

my_set = {1,2,3,4,3,2}
print(my_set)

# my_set ={1,2,[3,4]}       becz in tuples list cant be stored

# empty set
a = set()
print(type(a))

# add an element

my_set = {1,3}
my_set.add(2)
print(my_set)

# add multiple element

my_set.update([2,3,4])
print(my_set)

# add list and set

my_set.update([4,5],{1,6,8})
print(my_set)

# remove items

my_set = {1,3,4,5,6}
my_set.discard(4)
print(my_set)

# pop an element
my_set.pop()
print(my_set)

# clear my set
my_set.clear()
print(my_set)


