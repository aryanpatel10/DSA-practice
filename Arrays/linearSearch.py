def linearSearch(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i 
          
    return -1

#EXAMPLE 
nums = [1,2,3,4,3,5]
target = 5
print(linearSearch(nums,target))