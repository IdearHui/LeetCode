import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        dic = dict(collections.Counter(s).items())
        index = []
        for k, v in dic.items():
            if v == 1:
                index.append(s.index(k))
        if len(index) < 1:
            return -1
        return min(index)

if __name__ == "__main__":
    so = Solution()
    string = "loveleetcode"
    res = so.firstUniqChar(string)
    print(res)
