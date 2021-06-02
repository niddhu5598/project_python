def mean(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)

m1 = mean(1,2,3,4,5)
print(mean(1,2,3,4,5))
m2 = m1*20
print('meanx20',m2)


def word_counter(sentence):
    if sentence:
        words = sentence.split()
        count = len(words)
        return count
        

c1 = word_counter('')
c2 = word_counter('hi nidhi,what are you doing dear')

print(c1)
print(c2)