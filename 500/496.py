class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for fn in findNums:
            index = nums.index(fn)
            for n in range(index+1, len(nums)):
                if nums[n] > fn:
                    result.append(nums[n])
                    break
                elif n == len(nums)-1:
                    result.append(-1)
            if index+1 >= len(nums):
                result.append(-1)
            print(fn, index, result)
        return result

if __name__ == "__main__":
    s = Solution()
    # find_nums = [4, 1, 2]
    # big_nums = [1, 3, 4, 2]
    find_nums = [1,3,5,2,4]
    big_nums = [6,5,4,3,2,1,7]
    # find_nums = [1,3,5,2,4]
    # big_nums = [5,4,3,2,1]
    res = s.nextGreaterElement(find_nums, big_nums)
    print(res)
