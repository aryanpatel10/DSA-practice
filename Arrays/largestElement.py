""""
Given an array of integers nums, return the value of the largest element in the array

Example 1
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Example 2
Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99

""" 
nums = [2,3,4,1,9,4,7,0]
n = len(nums)
largest = nums[0]
for i in range(n):
    if nums[i] > largest:
        largest = nums[i]
        i += 1

print(largest)
