nums = [2,3,4,1,9,4,7,0]

n = len(nums)
largest = nums[0]
for i in range(n):
    if nums[i] > largest:
        largest = nums[i]
        i += 1

print(largest)
