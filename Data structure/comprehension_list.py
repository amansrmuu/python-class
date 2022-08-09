x= [2,4,7,8,9,6]
x2=[ i**2 for i in x]
print(x2)


# syntax for comprehension list
# newlist = [expression forloop  condition]

y = [2,3,47,6,75,8]
z =[i+j for i,j in zip(x,y)]
print(z)


names = ['bruce lee','clark kent','wally west']
initials =[]

for name in names:
    parts =name.split()
    initials.append(parts[0][0]+parts[-1][0])
print(initials)

initials = [name.split()[0][0]+name.split()[-1][0] for name in names ]
print(initials)

