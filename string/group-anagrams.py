class Solution(object):
    def groupAnagrams(self, strs):
        hashMap = {}
        for word in strs:
            characters = tuple(sorted(word))
            if characters not in hashMap:
                hashMap[characters] = [word]
            else: 
                hashMap[characters].append(word)
        return list(hashMap.values())