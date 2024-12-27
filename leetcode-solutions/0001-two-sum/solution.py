class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        for i in range(len(nums)):
            store[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in store and store[complement] != i:
                return [i, store[complement]]
            
        
