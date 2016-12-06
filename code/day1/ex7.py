from __future__ import division



data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
f = open('myfile.txt', 'wb')
string = ''
for num in data:
	string += "{}, {}, {} \n".format(str(num), str(num**2), str(num**2/(3.0)) )
f.write(string)
f.close()

with open('google-10000-english-no-swears.txt', 'rb') as f:
	w_lengths = [len(i.strip()) for i in f.xreadlines()]
	print sum(w_lengths)/len(w_lengths)


with open('google-10000-english-no-swears.txt', 'rb') as f:
	w_l_tup = [(len(i.strip()), i.strip()) for i in f.xreadlines()]
	print max(w_l_tup)