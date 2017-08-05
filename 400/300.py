from numpy import ones


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dp = ones(len(nums))
        for i in range(len(nums)):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(int(dp[i]), int(dp[j]) + 1)
                j += 1
            res = max(res, int(dp[i]))
        return res


if __name__ == "__main__":
    so = Solution()
    arrs = [10, 5, 7, 6, 8, 11]
    print(so.lengthOfLIS(arrs))
