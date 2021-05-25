def getSmallerElemCount(l,x):

    res = [i for i in l if i < x]
    count = len(res)
    return count

my_list = [4,5,3,1,2]
x = 3

#res = [i for i in my_list if i < x ]
#c = len(res)
print(getSmallerElemCount(my_list,x))
#print(c)

