class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if haystack.find(needle) != -1:
            sub_haystack = haystack.split(needle)[0]
            return len(sub_haystack)
        return -1