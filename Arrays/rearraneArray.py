#               REARRANGE ARRAY ELEMETNS BY SIGN
""" 
Given an array 'nums' of size even interger. Modify the array such that:
1. Every consecutive pair of integers have opposite sign.
2. Maintain the order of interger as they were present in the actual array
3. Modified array begins with the posiitve integer

Input: nums = [3,1,-2,-5,2,-4]
Output [3,-2,1-5,2,-4]; Order of positive integer:[3,1,2] & Order of negative integer: [-2,-5,-4]

"""
#                           BRUTE FORCE APPROACHED
# Store the order of positive and negative integer . Placed them one by one back to the main array in alternate order.

def rearrangeArray(nums):
    n = len(nums)
    positive = []
    negative = []
    for i in range(n):
        if nums[i] > 0:
            positive.append(nums[i]) # Storing the positve integer to record it's order
        else:
            negative.append(nums[i]) # Storing the negative integer to record it's order
    for i in range(n//2):
        nums[2*i] = positive[i]     
        nums[2*i+1] = negative[i]
    return nums

nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
