class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []
        for num in nums:
            myMap[num] = myMap.get(num, 0) + 1
        for n, c in myMap.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
