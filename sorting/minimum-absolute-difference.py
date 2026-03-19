class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[1] - arr[0]

        for i in range(1, len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < minDiff:
                minDiff = diff
        
        result = []
        for i in range(len(arr)-1): 
            if arr[i+1] - arr[i] == minDiff:
                result.append([arr[i], arr[i+1]])
        return result