def twoSum():
    nums=[3,2,4]
    target=6
    for j in range(0,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[j]+nums[k]==target:
                return j,k
twoSum()