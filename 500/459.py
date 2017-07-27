class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1


if __name__ == "__main__":
    so = Solution()
    st = "ababcabab"
    res = so.repeatedSubstringPattern(st)
    print(res)
