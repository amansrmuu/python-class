name = input('what is your name=>')

print(name)
print(f'length:{len(name)}')

cl_name = name.strip() #removing leading and trailing whitespaces or chars
print(f'length:{len(cl_name)}')

secret_msg = '0000000000000000OLA000000000000'
print(secret_msg.strip('0'))
print(secret_msg.lstrip('0'))
print(secret_msg.rstrip('0'))

crap_msg='''
    hey brother

'''
clean_msg = crap_msg.strip()
print(crap_msg)
print(clean_msg)