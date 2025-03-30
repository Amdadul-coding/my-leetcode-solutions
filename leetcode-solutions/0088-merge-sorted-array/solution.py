class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1 = m - 1
        num2 = len(nums2) - 1
        for i in range(m + n - 1, -1, -1):
            if num2 >= 0 and nums2[num2] > nums1[num1]:
                nums1[i] = nums2[num2]
                num2 -= 1
            elif num1 >= 0:
                nums1[i] = nums1[num1]
                num1 -= 1
            else:
                nums1[i] = nums2[num2]
                num2 -= 1

