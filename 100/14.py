class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, char in enumerate(shortest):
            for st in strs:
                if st[index] != char:
                    return shortest[:index]
        return shortest

if __name__ == "__main__":
    so = Solution()
    str_lists = ["ab", "abc", "a"]
    print(so.longestCommonPrefix(str_lists))
