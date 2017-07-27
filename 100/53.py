class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = max_ret = nums[0]
        for n in nums[1:]:
            ret = max(n, ret+n)
            max_ret = max(ret, max_ret)
        return max_ret

if __name__ == "__main__":
    s = Solution()
    n1 = [1, 2]
    num = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = s.maxSubArray(n1)
    print(res)
