class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))

if __name__ == "__main__":
    s = Solution()
    str1 = "13"
    str2 = "150"
    res = s.addStrings(str1, str2)
    print(res)
