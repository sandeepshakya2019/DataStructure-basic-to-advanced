def MissingNumber(nums):
    i = 0
    n = len(nums)
    while i < n:
        correctIdx = nums[i]
        if i != correctIdx and correctIdx < n:
            nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
        else:
            i = i + 1
    i = 0
    while i < n:
        if nums[i] != i:
            return i
        i = i + 1

def printallDisappered(nums):
    i = 0
    n = len(nums)
    while i < n:
        correctIdx = nums[i] - 1
        if nums[i] != nums[correctIdx] and correctIdx < n:
            nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
        else:
            i = i + 1
    print(nums)
    arr = []
    i = 0
    while i < n:
        if nums[i] != i + 1:
            arr.append(i + 1)
        i = i + 1
    return arr


def DuplicateNumber(nums):
    i = 0
    n = len(nums)
    while i < n:
        correctIdx = nums[i] - 1
        if nums[i] != nums[correctIdx] and correctIdx < n:
            nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
        else:
            i = i + 1
    print(nums)
    arr = []
    i = 0
    while i < n:
        if nums[i] != i + 1:
            arr.append(nums[i])
        i = i + 1
    return arr

nums = [4,3,2,7,8,2,3,1]
# print(MissingNumber(nums))
print(DuplicateNumber(nums))