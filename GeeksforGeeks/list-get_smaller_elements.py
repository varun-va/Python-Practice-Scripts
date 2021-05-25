# given x, print all the elements from the list l, which are smaller than x

def getSmaller(l, x):
    result = []

    for i in l:
        if i < x:
            result.append(i)
    return result



l = [8,100,20, 7, 40, 3,10]
x = 10
#print(getSmaller(l, x))

res = [i for i in l if i < x]
print(res)

