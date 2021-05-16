# This method  is the actual method for solving the reverse of the array
from array import *
arr = array("i",[1,2,3,4,5,6,7,8,9,10])
# print(len(arr))
def reverse(lst):
    start_index=0
    end_index=len(arr)-1
    while start_index<end_index:
        arr[start_index],arr[end_index]=arr[end_index],arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
reverse(arr)
print(arr)

# simple method for reverse array in from of list
mylist = [1,2,3,4,5,6]
print("This is my list before reverse ",mylist)
mylist.reverse()
print("This is mylist after reverse ",mylist)

# reverse the array using silicing technique
list1 = [1,2,3,5,6,7,8,9]
print("THIS IS ORIGINAL LIST",list1)
list2 = list1[::-1]
print("This is the reverse list",list2)
