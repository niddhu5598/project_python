def remove_punc(sentence,punctuation ='!@#$%^&*(),_+"[]'):
    for item in punctuation:
        if item in sentence:
            sentence = sentence.replace(item,'')
    print(sentence)

msg = " hi there,)(!@#$%^&*(*(*&^%$where ideas th[])(*&^%$#@@@@@!@#$%treasure."
remove_punc(msg,'()*&^%$#@!')
remove_punc(msg)



def sum(a,b,c,d=0):
    print(a+b+c+d)

sum(12,3,6)
sum(5,4,3,2)
sum(a=4,b=2,c=5)