class Solution(object):
    def firstUniqChar(self, s):
        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
        for i, char in enumerate(s): 
            if hashMap[char] == 1:
                return i
        return -1
        