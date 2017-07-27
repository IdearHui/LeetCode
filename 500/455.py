class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)[::-1]
        s = sorted(s)[::-1]
        print(g, s)
        res = 0
        j = 0
        for i in range(len(g)):
            while j < len(s):
                if s[j] >= g[i]:
                    res += 1
                    j += 1
                break
            print(i, j, res)
        return res

if __name__ == "__main__":
    so = Solution()
    gg = [1, 3, 1]
    ss = [1, 2, 1]
    result = so.findContentChildren(gg, ss)
    print(result)
