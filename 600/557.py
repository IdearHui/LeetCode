class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sent_list = s.strip().split()
        sent_result = ""
        for i, sen in enumerate(sent_list):
            if i < len(sent_list)-1:
                sent_result += sen[::-1] + " "
            else:
                sent_result += sen[::-1]
        return sent_result


if __name__ == "__main__":
    so = Solution()
    st = " A boy is playing a basketball"
    res = so.reverseWords(st)
    print(res)
