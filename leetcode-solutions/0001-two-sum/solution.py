class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in my_map:
                return[i, my_map[j]]
            my_map[nums[i]] = i
