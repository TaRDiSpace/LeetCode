class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        elif x < 10:
            return True

        length = 1
        while x / length >= 10:
            length *= 10
        while x != 0:
            l = x / length
            r = x % 10
            if l != r:
                return False
            x = (x % length) / 10
            length /= 100

        return True
