class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        add = 1
        for i, d in enumerate(digits):
            if d+add > 9 and i < len(digits)-1:
                digits[i] = (d+add) % 10
                add = int((d+add) / 10)
            elif d+add > 9 and i == len(digits)-1:
                digits[i] = (d+add) % 10
                digits.append(int((d+add) / 10))
                break
            else:
                digits[i] = d+add
                break
        return digits[::-1]

if __name__ == "__main__":
    s = Solution()
    dig = [9, 1]
    res = s.plusOne(dig)
    print(res)
