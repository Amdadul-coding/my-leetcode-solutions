class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        righta = len(a) - 1
        rightb = len(b) - 1
        while righta >= 0 or rightb >= 0 or carry:
            if righta >= 0:
                carry += int(a[righta])
                righta -= 1
            if rightb >= 0:
                carry += int (b[rightb])
                rightb -= 1
            print(carry)
            result = str(carry % 2) + result
            carry //= 2
        return result

