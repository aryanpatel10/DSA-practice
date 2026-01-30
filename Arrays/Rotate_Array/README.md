"""
def rotateArray(nums,k):
    n = len(nums)
    k = k % n
    temp = []
    i= 0
    while i <= k:
        temp.append(nums[i])
        i += 1
    #Shifting
    for i in range(k,n):
                                                         #This is the brute force method 
        nums[i-k] = nums[i]

    # j = 0   this can be written as  i-(n-k)
    for i in range(n-k,n):  # i = [n-k = 4] to n = 7 
            nums[i] = temp[i-(n-k)]
            
    return nums
#EXAMPLE
k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,6]
rotate = rotateArray(nums,k)
print(rotate)

"""


# Optimal mehtod
def rotateArray(nums,k):
    n = len(nums)
    k = k%n
    first = nums[:n-k]
    first.reverse()

    second = nums[n-k:]
    second.reverse()

    result = first + second
    result.reverse()
    
    return result

#EXAMPLE
k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,7]
rotate = rotateArray(nums,k)
print(rotate)