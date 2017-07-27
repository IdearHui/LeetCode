class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))

if __name__ == "__main__":
    s = Solution()
    nums_list = [4, 2, 3, 3, 5]
    result = s.findDisappearedNumbers(nums_list)
    print(result)
