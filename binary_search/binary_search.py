def BinarySearchRecursive(nums, target, low, high):
    if low > high:
        return 
    
    mid = low + (high - low ) // 2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        high = mid - 1
        BinarySearchRecursive(nums, target, low , high)
    else:
        low = mid + 1
        BinarySearchRecursive(nums, target, low, high)
