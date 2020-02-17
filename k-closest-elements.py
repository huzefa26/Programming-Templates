'''
Find the k elements that are closest to x in an array
'''

def findClosestElements(nums, k, x):
    if len(nums) == 0 or k == 0:
        return []
    if len(nums) <= k:
        return nums
    left, right = 0, len(nums) - k
    while left < right:
        mid = (left + right) // 2
        # print(nums[left : left + k])
        # print(nums[left], nums[mid], nums[mid+k], nums[right])
        if x - nums[mid] > nums[mid+k] - x:
            left = mid + 1
        else:
            right = mid
    
    return nums[left : left + k]


nums = [0,1,1,1,2,3,6,7,8,9]
k = 9
x = 4

print(findClosestElements(nums, k, x))

nums = [1,2,3,4,5]
k = 4
x = -1

print(findClosestElements(nums, k, x))

nums = [1,1,1,10,10,10]
k = 1
x = 9

print(findClosestElements(nums, k, x))

nums = [0,2,2,3,4,6,7,8,9,9]
k = 4
x = 5

print(findClosestElements(nums, k, x))
