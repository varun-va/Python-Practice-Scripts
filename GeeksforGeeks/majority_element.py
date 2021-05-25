'''
Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y. 
If both elements have the same frequency, then return the smaller element.

Note:  We need to return the element, not its count.

Example 1:

Input:
N = 11
arr[] = {1,1,2,2,3,3,4,4,4,4,5}
x = 4, y = 5
Output: 4
Explanation: 
frequency of 4 is 4.
frequency of 5 is 1.
 

Example 2:

Input:
N = 8
arr[] = {1,2,3,4,5,6,7,8}
x = 1, y = 7
Output: 1
Explanation: 
frequency of 1 is 1.
frequency of 7 is 1.
Since 1 < 7, return 1.
'''

def getMajority(arr, x, y):

    c1 = arr.count(x)
    c2 = arr.count(y)
    print('c1: ', c1)
    print('c2: ', c2)

    if c1 > c2:
        return x
    elif c1 == c2:
        if x < y:
            return x
        else:
            return y
    else:
        return y


arr1 = [1,1,2,2,3,3,4,4,4,4,5]
x1 = 4
y1 = 5

arr2 = [1,2,3,4,5,6,7,8]
x2 = 1
y2 = 7

arr = [5, 22, 29, 12, 32, 69, 1, 75]
x = 29
y = 96
print(getMajority(arr, x, y))
