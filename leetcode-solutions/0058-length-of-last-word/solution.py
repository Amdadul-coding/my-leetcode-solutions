class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split()
        print(s)
        if len(s) == 0:
            return 0
        return len(s[-1])
