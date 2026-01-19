#This repo contains the logic that how different sorting algorithms work.

#"iss algo m ek-ek element ko ek-ek kar k unki sahi positiion m place krte hai...by comparing and swapping it position from its adjacent element."


In Bubble sort algorith,what we do is :
1. We start from the beginning of the array i.e. nums[i]    # i = 0
2. We comapre it from it's adjacent element i.e. nums[i+1]
3. If nums[i]< nums[i+1]. then swap
4. Else increase i by 1 i.e. i = i+1
5. After one full pass, the largest element moves at the end.
6. Repeat till array is sorted.


#STEPS
1. Repeat for i = 0 to n:
2. Set swapped = false
3. For j = 0 to n-i-1:
4.      If arr[j] > arr[j+1]:
5.          Swap arr[j] and arr[j+1]
6.          Set swapped = true
7. If swapped is false:
8.  Break (array is already sorted)


#EXample
nums = [5,1,4,2]

pass 1: [1,5,4,2] ---> [1,4,5,2]---> [1,4,2,5]
pass 2: [1,4,2,5] ---> [1,2,4,5]
pass 3: No swap = Sorted array


#IMPLEMENTATION

def bubble_sort(nums):
    n = len(nums)
    for i in range (n):
        isSwap = False
        for j i range (0,n-i-1):
            if nums[j]>nums[j+1]:
                #swap
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                isSwap = True
        if not isSwap:
            break
    return nums


    #Time Complexity
    Best case = O(n) In case ,array is already sorted
    Average case = O(n²) 
    Worst Case = O(n²)

    #Sapce Complexity = O(1) No new array is formed



