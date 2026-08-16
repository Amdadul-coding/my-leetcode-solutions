class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        print(hashMap)
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashMap and hashMap[result] != i:
                return [i, hashMap[result]]

