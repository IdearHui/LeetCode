class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        if len(s) <= k:
            return s[::-1]
        gap = len(s)/k + 1
        for n in range(gap):
            if n % 2 == 0:
                res += self.reverseStr(s[n*k:(n+1)*k], k)
            else:
                res += s[n*k:(n+1)*k]
        if k < len(s) % (2*k) < (2*k):
            res += self.reverseStr(s[gap*k:], k)
        return res

if __name__ == "__main__":
    s = Solution()
    s1 = "abcdefghij"
    s2 = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    result = s.reverseStr(s2, 39)
    print(result)
