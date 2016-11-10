"""
For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            if count and s[i] == ' ':
                return count
        return count
