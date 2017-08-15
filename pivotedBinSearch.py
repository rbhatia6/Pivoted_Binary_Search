#!/usr/bin/env python

def findPivot(myList, low, high): 
    mid = int((low + high)/2)
    if ((mid < high) and (myList[mid] > myList[mid+1])):
        return mid
    if ((mid > low) and (myList[mid] < myList[mid+1])):
        return mid-1
    if myList[low] >= myList[mid]:
        return findPivot(myList, low, mid-1)
    return findPivot(myList, mid+1, high)
    
    
def pivotedBinSearch(myList, n, num):
    pivot = findPivot(myList, 0 , n-1)
    
    if pivot == -1:
        return binSearch(myList, 0, n-1, num)
    
    if (myList[pivot] == num):
        return pivot
    if myList[0] <= num:
        return binSearch(myList, 0, pivot-1, num)
    return binSearch(myList, pivot+1, n-1, num)

def binSearch(myList, low, high, num):
    if (high < low):
        return -1
    mid = int((low+high)/2)
    if (myList[mid] == num):
        return mid
    if (myList[mid] < num):
        return binSearch(myList, mid+1, high, num)
    return binSearch(myList, low, mid-1, num)


myList=[5,6,7,1,2,3,4]
n = len(myList)
num = 6
print(pivotedBinSearch(myList, n, 7))
