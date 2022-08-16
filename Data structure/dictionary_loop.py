squares = {1: 1,2: 4,3: 9,4: 16,5: 25}

# only keys

for i in squares:
    print(i)

# only values using i as key

for i  in squares:
    print(squares[i])

# using item function to get both key and value

for k,v in squares.items():
    print(k,v)

