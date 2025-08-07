class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}
        for chs,cht in zip(s,t):
            counts_s[chs] = counts_s.get(chs, 0) + 1
            counts_t[cht] = counts_t.get(cht, 0) + 1
        return counts_s == counts_t
        
