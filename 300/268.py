class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        print(nums)
        for i, n in enumerate(nums):
            if n > i:
                return i
        else:
            return len(nums)

if __name__ == "__main__":
    s = Solution()
    lists = [1, 0]
    res = s.missingNumber(lists)
    print(res)