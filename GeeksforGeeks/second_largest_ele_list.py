
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

def getSecMax(l):
    # 2 traversal of list
    if len(l) <= 1:
        return None
    lar = getMaxLinear(l)
    sec = None

    for x in l:
        if x != lar:
            if sec == None:
                sec = x
            else:
                sec = max(sec, x)
    return sec


l1 = [20, 10, 20,8, 12]

l2= [10,10,10]

print(getSecMax(l2))