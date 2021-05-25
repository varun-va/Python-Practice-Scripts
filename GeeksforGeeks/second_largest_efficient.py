def getSecMaxlin(l):
    if len(l) <= 1:
        return None
    
    lar = l[0] # first element is considered as largest to begin with
    sec = None

    for x in l[1:]:
        if x > lar:
            sec = lar
            lar = x
        elif x != lar:
            if sec == None or sec < x:
                sec = x
    return sec

l1 = [20, 10, 20,8, 12]

l2= [10,10,10]

l3 = [4,67,13,12,15]

print(getSecMaxlin(l3))