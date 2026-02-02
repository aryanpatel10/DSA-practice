def moveZeros(nums):
    #suppose No zeros are in the array
    j = -1   
    n = len(nums)
    #Place the j where first zero appears
    for i in range(n):
        if nums[i] == 0:
            j = i                 
            break
    #IF no zeros are there
    if j == -1:
        return nums
    #Swap the non-zero element with zeros
    for i in range(j+1,n):
        if nums[i] != 0:
            nums[j],nums[i] = nums[i], nums[j]
            j +=1
    return nums

#EXAMPLE
nums = [1,0,1]
moveZeros(nums)
print(nums)

