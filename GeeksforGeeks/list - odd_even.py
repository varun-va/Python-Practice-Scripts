def getEvenOdd(l):

    odd = []
    even = []

    if len(l) > 0:
        for x in l:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
    else:
        even = 0
        odd = 0
    return even, odd

def getEvenOddlc (l):
    even =[x for x in l if x % 2 == 0]
    odd = [x for x in l if x % 2 != 0]

    return even, odd

l1 = [10,12,11,16]
l =[]
#even, odd = getEvenOdd(l)
even,odd = getEvenOddlc(l1)
print(even)
print(odd)
