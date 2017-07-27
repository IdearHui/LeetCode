class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)

if __name__ == "__main__":
    s = Solution()
    lists = [1, 2, 2147483647]
    res = s.minMoves(lists)
    print(res)
