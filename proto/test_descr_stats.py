


#Functions to test

def mean_stat(nums):
    return sum(nums)/len(nums)

def median_stat(nums):
    nums.sort()
    cnt = len(nums)
    mid = int(cnt/2)
    if cnt%2 == 0:
        return (nums[mid] + nums[mid-1])/2
    else:
        return nums[mid]