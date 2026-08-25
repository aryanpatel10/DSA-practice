#Transpose the given matrix or 2D list
nums  = [[10,25,30],
        [7,12,15],]

rows = len(nums)
cols = len(nums[0])

res = [[0]*rows  for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        res[j][i] = nums[i][j]
print(res)