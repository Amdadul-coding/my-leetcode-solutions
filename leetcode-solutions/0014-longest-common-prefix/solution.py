class Solution(object):
    def longestCommonPrefix(self, strs):
        empty = ""
        sort = sorted(strs)
        first = sort[0]
        last = sort[-1]
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return empty
            empty += first[i]
        return empty
        
