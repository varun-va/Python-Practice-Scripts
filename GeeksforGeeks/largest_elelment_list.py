def getMax(l):
    # Time complexity: O(n*2)


    for x in l:
        for y in l:
            if y > x:
                break
        else:# else can be added to a FOR loop in Python
            return x
    return None

    #return [i for i in l if i > l]

def getMaxLinear(l):
    # lineat:  theta N

    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]
        return res



l1 = [10, 5, 20 , 8]
l2 =[]
print(getMax(l1))
print(getMaxLinear(l2))