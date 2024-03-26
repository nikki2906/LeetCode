class Solution(object):
    def groupAnagrams(self, strs):
        hashMap = {}
        for word in strs:
            char = tuple(sorted(word))
            if char not in hashMap:
                hashMap[char] = [word]
            else:
                hashMap[char].append(word)
        return list(hashMap.values())
        