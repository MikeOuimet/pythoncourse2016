def RemoveDoubles(data):
    list = []
    for point in data:
        if point not in list:
            list.append(point)
    return list

def SumUpTo(n):
    return sum(range(n+1))


def IsPerfect(n):
    divisors = []
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
    if sum(divisors) == n:
        return True
    else:
        return False


def subsets(list):
    sublists = []
    for i in range(2**len(list)):
        binary = '00'*len(list) + bin(i)[2:]
        binary = binary[-len(list):]
        #print binary
        subel = []
        for loc in range(len(list)):
            if int(binary[loc]) == 1:
                subel.append(list[loc])
        sublists.append(subel)
    return sublists

def sorted_sublists(sublists):
    return sorted(sublists)[1:]

def reversedict(d):
    keys = d.keys()
    vals = d.values()
    rd = {}
    for val in vals:
        out =[]
        for key in keys:
            if d[key] == val:
                out.append(key)
        rd[val] = out
    return rd


'''

data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]

#print RemoveDoubles(data)


#print SumUpTo(4)

#print IsPerfect(28)

#sublists =  subsets([0, 1, 2])
print sublists



print sorted_sublists(sublists)


'''

d = {i:(i%3) for i in range(10)}

print d

print reversedict(d)

