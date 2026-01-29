""" 
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.


Example 1
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation:
The largest value in nums is 8, the second largest is 7

Example 2
Input: nums = [10, 10, 10, 10, 10]
Output: -1
Explanation:
The only value in nums is 10, so there is no second largest value, thus -1 is returned

"""

nums = [8, 8, 7, 6, 5]
n = len(nums)
largest = nums[0]
second_largest = -1
for i in range(n):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
        i +=1
    else:
        if nums[i]< largest and nums[i]> second_largest:
            second_largest = nums[i]

    

print(second_largest)
