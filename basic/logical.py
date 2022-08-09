name = "sameer"
age = 16
pwd ="12345"

result = name == 'sameer' and pwd == '12345'
print(result)


amt = int(input('how much kg of apples u want?'))

if amt>=5:
    price = 80
else:
    price = 90
total = amt*price
print(f"you have to pay rs {total} for {amt} kg of apple")