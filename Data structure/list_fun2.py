
# count function

x = [1,1,1,1,1,2,3,3,3,4,7,9,0,7,5,4,2]
print(x.count(1))
print('total no of 3 =',x.count(3))
print('total no of 4x=',x.count(4))

movies = ['batman','ddlj','krish','3 idiot','rrr','kgf','doctor srange','avengers','dhoom']
print(movies.index('doctor strange'))
print(movies.index('kungfu panda'))

# copy function

blockbusters = movies.copy()
print('duplicated list = ', blockbusters)

# clear function

blockbusters.clear()
print('after clearing blockbusters =',blockbusters)

# pop function

print('after poping =',movies.pop())
print('after poping index 4 = ',movies.pop(4))
print('after poping index 7 =',movies.pop(7))
print('after poping unavailabe index = ',movies.pop(11))