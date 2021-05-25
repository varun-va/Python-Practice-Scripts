'''
    Script to find the 2 largest numbers in a list
'''
#nums = (47,11,42,102,13)
#a = [int(x) for x in nums.split()]
#print a

'''
n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        secondlargest = largest
        largest = x
    elif x > secondlargest and x != largest:
        secondlargest = x
print(largest)
print(secondlargest)
'''

nums = (47,11,11,42,102,13,11,13)
max1 = max2 = 0
for x in nums:
    print 'x is '+str(x)
    print 'max1 is '+str(max1)
    print 'max2 is '+str(max2)
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

print nums
print max1
print max2
