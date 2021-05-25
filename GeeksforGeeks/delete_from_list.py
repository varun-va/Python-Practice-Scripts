def deleteElement(l):
    new_list = []

    for i in l:
        #print(i)
        if i != "Tiya":
            new_list.append(i)
    l = new_list
    l.append(0)
    return l

def deleteElementIndex(l, n):

    del l[n]
    l.append(0)
    return l

my_list = [12, 'Siya', 'Tiya', 14, 'Riya', 12, 'Riya']

#By passing index as 2 to remove Tiya
#name = my_list.pop(2)
print(my_list)

print(deleteElement(my_list))

print(deleteElementIndex(my_list, 3))