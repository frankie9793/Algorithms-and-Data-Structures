def removeDuplicates(nums):
    
    # initial next item is the index 1
    nextItem = 1

    # Empty array
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[nextItem] = nums[i]
            nextItem += 1
    print(nums)
    return nextItem

nums = [0,1,1,2,2,2,3,3,4,4]
removeDuplicates(nums)

# Since the array is already sorted, we can keep two pointers i and j, 
# where i is the slow-runner while j is the fast-runner. 
# As long as nums[i] = nums[j], we increment j to skip the duplicate.

# When we encounter nums[j] != nums[i], nums[j] =nums[i], 
# the duplicate run has ended so we must copy its value to nums[i + 1]nums[i+1]. 
# i is then incremented and we repeat the same process again until j reaches the end of array.

# Time Complexity: O(n) we only iterate the array once where n is the length of array
# Space Complexity: O(1) no extra space used 
