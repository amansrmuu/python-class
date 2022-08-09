s ='digipodium'
slice1 = s[4:7]
print(slice1)


s = 'digipodium'
slice1 = s[0:4]
slice2 = s[:4]
print(slice1)
print(slice2)

slice1 = s[4:len(s)]
slice2 = s[4:]
print(slice1)
print(slice2)

name = 'aman kumar singh'
firstname = name[:-4]
print(firstname)
lastname = name [-4:]
print(lastname)
middlename = name[6:-8]
print(middlename)
even_index = name[::2]
print(even_index)
odd_index = name[1::2]
print(odd_index)
#reversing a swquence with slicing
reversed_name = name[::-1]
print(reversed_name)
print(name[:]) #wont affect
print(name[::-1][:7][::-1])

