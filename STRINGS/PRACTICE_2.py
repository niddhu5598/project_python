msg = 'brandon sanderson is an American author'
vowel = ['a','e','i','o','u']
for i in msg:
    if i in vowel:
        msg = msg.replace(i,'')
print(msg)        



msg = 'brandon sanderson is an American author'
vowel = ['a','e','i','o','u']
ln = 0
for i in msg:
    if i in vowel:
        ln +=1
print(ln)
