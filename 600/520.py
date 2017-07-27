class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        count = 0
        for wo in word:
            if wo.isupper():
                count += 1
        if count == len(word) or (count == 1 and word[0].isupper()) or count == 0:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    sent = "aH"
    res = s.detectCapitalUse(sent)
    print(res)
