# def SubArrayWithK(arr, neededSum):
#     mainLength = 0
#     for i in range(len(arr)):
#         sumitem = 0
#         for j in range(i, len(arr)):
#             sumitem += arr[j]
#             if sumitem == neededSum:
#                 length = j - i + 1
#                 mainLength = max(mainLength, length)
#     return mainLength

# def SubArrayWithK(arr, k):
#     mainlength = 0
#     prefixsum = 0
#     hashmap = {}

#     for i in range(len(arr)):
#         prefixsum = prefixsum + arr[i]
#         if prefixsum not in hashmap:
#             hashmap[prefixsum] = i
#         if prefixsum == k:
#             if hashmap.get(prefixsum - k):
#                 mainlength = max(mainlength, i - hashmap[prefixsum - k] )
#             else:
#                 mainlength = i + 1
#         if prefixsum > k:
#             if prefixsum - k in hashmap:
#                 mainlength = max(mainlength, i - hashmap[prefixsum - k] )

#     return mainlength

# def SubArrayWithK(arr, k):
#     n = len(arr)
#     i = 0
#     j = 0
#     sumofelem = 0
#     mainlen = 0
#     count = 0
#     while i < n and j < n:
#         sumofelem = sumofelem + arr[j]
#         if sumofelem == k:
#             count = count + 1
#             mainlen = max(mainlen, j - i + 1)
#         if sumofelem > k:
#             sumofelem = sumofelem - arr[i]
#             i = i + 1
#             if sumofelem == k:
#                 count = count + 1
#                 mainlen = max(mainlen, j - i + 1)
#         j = j + 1

#     return count

from collections import defaultdict

class Solution(object):
    def subarraySum(self, arr, k):
        count = 0
        prefixsum = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1  # to handle cases where prefixsum == k

        for num in arr:
            prefixsum += num
            count += hashmap[prefixsum - k]
            hashmap[prefixsum] += 1

        return count


# arr = [1,2,3]
# k = 3
# print(SubArrayWithK(arr, k))