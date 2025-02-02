def twoSum(nums: list[int], target: int)->list[int]:
    
    index_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    
    return []







nums = [2, 7, 11, 15] 
target = 9
print(twoSum(nums, target))

