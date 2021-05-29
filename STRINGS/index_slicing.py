name = 'nidhi chaubey pandey '
fname = name[0:5]
print(fname)

mname = name[6:14]
print(mname)

lname = name[14:-1]
print(lname)

# better version of fname and lname slice
fname = name[:5]
lname = name[-7:]
print(fname,lname)


print(name[:])         # fullname

print(name[:: -1])    # reverse the name