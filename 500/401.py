import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    ret.append('%d:%02d' % (h, m))
        return ret

if __name__ == "__main__":
    s = Solution()
    res = s.readBinaryWatch(2)
    print(res, len(res))