class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if (c == "{") or (c == "[") or (c == "("):
                stack.append(c)
            elif stack:
                if c == "}" and stack.pop() == "{":
                    continue
                elif c == "]" and stack.pop() == "[":
                    print(stack)
                    continue
                elif c == ")" and stack.pop() == "(":
                    continue
                else:
                    print("---")
                    return False
        if stack:
            return False
        return True

if __name__ == "__main__":
    so = Solution()
    st = "]"
    print(so.isValid(st))
