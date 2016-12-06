from __future__ import division 
data = "Mary had a little lamb its fleece was white as snow and everywhere that Mary went the lamb was sure to go"

words = data.split()
#print words

single_words = set(words)

word_lengths = [len(word) for word in words]
print sum(word_lengths)/len(word_lengths)


#single_words =  list(single_words)

single_words_lengths = [len(word) for word in single_words]

print sum(single_words_lengths)/len(single_words_lengths)


