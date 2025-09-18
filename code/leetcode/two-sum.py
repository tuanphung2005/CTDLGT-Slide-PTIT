def twoSum(nums, target):

    numsDict = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in numsDict:
            return [numsDict[comp], i]
        
        numsDict[nums[i]] = i
    return []

nums = [2,7,11,15] 
target = 9

print(twoSum(nums, target))