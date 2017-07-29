class Solution(object):
    def getCombination(self, values, result):
        tmp = []
        for val in values:
            if len(result) == 0:
                tmp.append(val)
            for res in result:
                tmp.append(res+val)
        return tmp

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maps = {"0": " ", "1": "*", "2": "abc", "3": "def", "4": "ghi",
                "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        for d in digits:
            result = self.getCombination(maps[d], result)
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.letterCombinations("23")
    print(r)
