my_tuple = (1,'hello,3.4')
print(my_tuple)

my_tuple = ('mouse',[8,4,6],(1,2,3))
print(my_tuple)

my_tuple = 3,4.8,'apple'
print(my_tuple)


# tuple element using indexing

my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple

n_tuple = ('mouse',[2,3,5],(1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])

# slicing in tuple

my_tuple = ('e','x','c','a','l','i','b','u','r')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

# concatenation
print((1,2,3)+(4,5,6))

# repeat
print(('repeat',)*3)

# count and index
my_tuple = ()
print(my_tuple.count('p'))
print(my_tuple.index('1'))
