class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        sn = bin(num).split("0b")[1]
        print(sn, len(sn))
        count = 0
        if sn[0] == "1" and len(sn) > 2 and len(sn) % 2 == 1:
            for n in sn:
                if n == "1":
                    count += 1
        if count == 1:
            return True
        return False

if __name__ == "__main__":
    so = Solution()
    res = so.isPowerOfFour(1073741824)
    print(res)