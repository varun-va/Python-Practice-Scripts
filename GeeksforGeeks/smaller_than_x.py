'''
Given an array arr[] of size N containing positive integers and an integer X, 
find the element in the array which is smaller than X and closest to it.

Example 1:

Input:
N = 5
arr[] = {4 67 13 12 15}
X = 16
Output: 15
Explanation: 
For a given value 16, there are four values which are smaller than
it. But 15 is the number which is smaller and closest to it with minimum difference of 1.
 

Example 2:

Input:
N = 5
arr[] = {1 2 3 4 5}
X = 1
Output: -1
Explanation: No value is smaller than 1.

def immediateSmaller(arr,n,x):
#return required ans

'''
def getSmaller(l,x):

    res = [i for i in l if i < x]
    if len(res) > 0:
        return max(res)
    else:
        return -1

    '''res = -1
    for i in l:
        if i < x:
            res = i
    return res'''

my_list = [4,67,13,12,15,17]
x = 20

my_list1 = [10,10,10,10]
x1 = 10

l2 = [3168,256,180,2208,1717,5006,4726,2728,7886,1,9128,5921,59,2174,4639,7528,8006,7483,6114,7005,1730,8862,9669,9825,2315,1449,2280,8752,7456,5007,3520,624,1615,52,9184,9685,5058,262,8765,9297,263,4245,1570,6674,6419,6209,4202,778,45,6669,7783,8127,5531,7452,7953,4199,5254,6585,2951,2710,7944,2823,9687,9560,2876,5223,5597,4286,5486,4362,3583,2101,8607,1506,8776,1378,4067,2978,2156,4112,9647,6292,2240,1531,96,193,5730,5350,3130,5033,4413,1075,7856,452,635,732,5675,2584,5019,7513,6946,4954,9615,19
 ]
x = 727

print(getSmaller(l2, x))