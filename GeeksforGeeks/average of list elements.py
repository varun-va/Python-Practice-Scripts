# mean of list elements

def mean(l):
    sum = 0
    for i in l:
        sum = sum + i

    n = len(l)
    return sum/n

l = [10,20,30,40]
print(mean(l))