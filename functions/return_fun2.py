def word_counter(sentence):
    if sentence:
        words = sentence.split()
        count = len(words)
        return count
from string import punctuation

def clean_punc(sentence):
    for char in punctuation:
        sentence=sentence.replace(char,'')
    return sentence
        
c1 = word_counter('')
c2 = word_counter('hi n,i,d,h,i,wh,at ar,,e you doing dear')

print(c1)
print(c2)