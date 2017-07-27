class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0:
            return False
        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(2147412))
