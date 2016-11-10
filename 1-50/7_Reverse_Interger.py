"""
Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        while x > 0:
            res = (res * 10) + (x % 10)
            x = x // 10
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return flag * res
