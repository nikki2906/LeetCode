class Solution(object):
    def topKFrequent(self, nums, k):
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        sortedNum = sorted(hashMap, key = hashMap.get, reverse = True)
        return sortedNum[:k]
            