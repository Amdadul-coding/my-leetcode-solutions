class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        val_set = set(nums)
        return len(nums) > len(val_set)
