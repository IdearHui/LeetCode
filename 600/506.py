class Solution(object):
    """
    Given scores of N athletes,
    find their relative ranks and the people with the top three highest scores,
    who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal"
    """
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        new_nums = sorted(nums)
        new_nums = new_nums[::-1]
        maps = {}
        for n in range(len(nums)):
            maps[n] = nums.index(new_nums[n])
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = [0]*len(nums)
        for k, v in maps.items():
            if k <= 2:
                res[v] = medal[k]
            else:
                res[v] = str(k+1)
        return res


if __name__ == "__main__":
    s = Solution()
    lists = [10, 3, 8, 9, 4]
    result = s.findRelativeRanks(lists)
    print(result)
