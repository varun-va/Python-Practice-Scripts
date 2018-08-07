'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given number is inside the list and returns (then prints)
an appropriate boolean.
Extras:
Use binary search.
'''


def user_input():
    num_list = input("Enter list of numbers, seperated by spaces: ").split()
    num_list = [int(v) for v in num_list]
    num_list.sort()
    return num_list

num_list=user_input()
print(num_list)
finder = int(input("Enter a number to be searched from that above list: "))
#print("Number to search: " + str(finder))

def find_number(finder,num_list):
    for num in num_list:
        #print(str(num))
        if num == finder:
            #print('The number '+str(finder)+ ' is present in the list')
            return True
    return False


result = find_number(finder,num_list)

print(result)

#5 9 1 3 25 20 46 35
