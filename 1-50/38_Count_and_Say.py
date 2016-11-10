"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
"""


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n <= 1:
            return '1'

        def count(s):
            tmp, count, p = '', 0, '$'
            for i in s:
                if i != p:
                    if p != '$':
                        tmp += str(count) + x
                        x = i
                    count = 1
                    p = i
                else:
                    count += 1
                x = i
            tmp += str(count) + i
            return tmp

        s = '1'
        for i in range(2, n + 1):
            s = count(s)
        return s
