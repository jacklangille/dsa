def binary_search(nums: list[int], target: int) -> int:
    low = 0    
    high = len(nums) -1
    
    while low <= high:
        mid = (low + high) // 2 

        if target < nums[mid]:
             high = mid -1
        elif target > nums[mid]:
            low = mid + 1 
        else:
            return mid

    return -1


    








print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 3))
