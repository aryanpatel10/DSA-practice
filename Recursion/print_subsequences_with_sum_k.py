#                   PRINT ALL THE SUBSEQUENCES WHOSE SUM = K

def subsequence(indx,nums,subs,curr_sum,k):
    n = len(nums)
    # BASE CASE
    if indx == n:
        if curr_sum == k:
            print(subs)
        return

    # PICK ELEMENT
    subs.append(nums[indx])
    curr_sum += nums[indx]
    subsequence(indx+1,nums,subs,curr_sum,k)

    #BACK TRACKING
    subs.pop()
    curr_sum -= nums[indx]

    # NOT PICK ELEMENT
    subsequence(indx+1,nums,subs,curr_sum,k)

nums = [1,2,1]
k = 2
subsequence(0,nums,[],0,k)



#                           TYPE 2: PRINT ANY ONE SUBSEQUENCE WITH SUM = K

def subsequence(indx,nums,subs,curr_sm,k):
    n = len(nums)
    # BASE CASE
    if indx == n:
        if curr_sm == k:
            print(subs)
            return True
        return False
    
    # PICK ELEMENT
    subs.append(nums[indx])
    curr_sm += nums[indx]
    if subsequence(indx+1,nums,subs,curr_sm,k):
        return True

    # BACK TRACK
    subs.pop()
    curr_sm -= nums[indx]

    # NOT PICK ELEMENT
    if subsequence(indx+1,nums,subs,curr_sm,k):
        return True
    return False

nums = [1,2,1]
k = 2
subsequence(0,nums,[],0,k)

