def merge_arr(left,right):
    result = []
    i = j = 0
    n = len(left)
    m = len(right)

    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    if i<n:
        while i<n:
            result.append(left[i])
            i += 1
    if j<m:
        while j<m:
            result.append(right[j])
            j +=1
    return result

def Merge_sort(nums,low,high):
    #Base case
    if low >= high:
        return [nums[low]]

    #Recursive case
    mid  = (low+high)//2
    left = Merge_sort(nums,low,mid)
    right = Merge_sort(nums,mid+1,high)
    sorted_array = merge_arr(left,right)
    
    return sorted_array

# Example Usa Case

array = [3,2,4,1,3]
print(f"Given array: {array}")

sorted_array = Merge_sort(array,0,len(array)-1)
print(f"Sorted array: {sorted_array}")
