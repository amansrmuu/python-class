# union set operator

a = {1,2,3,4,5,6}
b = {4,5,6,7,8}

print(a|b)

# use union function

a.union(b)
print(a.union(b))

# intersection set

print(a&b)

# subset operator

x = {2,3,4,7}
y = {2,3,4,7,6,5,8}
print(x.issubset(y))

z = {3,5,8,10,11}
print(x.issubset(z))

k = {11,12,13}
print(k.isdisjoint(k))

# use intersection function

a.intersection(b)
print(a.intersection(b))

# set difference

print(a - b)

# use differnce function on a

a.difference(b)
print(a.difference(b))

# set symmetric difference

print(a^b)

# use symmetric function on a

a.symmetric_difference(b)
print(a.symmetric_difference(b))

# duplicates sets

h = [2,2,3,5,5,6,6]
hs = set(h)
hl = list(set(h))
print(h)
print(hs)
print(hl)