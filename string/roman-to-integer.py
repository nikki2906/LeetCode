class Solution(object):
    def romanToInt(self, s):
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and hashMap[s[i]] < hashMap[s[i+1]]:
                result -= hashMap[s[i]]
            else:
                result += hashMap[s[i]]
        return result