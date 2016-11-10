class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if x == 0:
            return float(0)
        if x == 1:
            return float(1)
        if n == 0:
            return float(1)
        if x == -1:
            if n % 2 == 0:
                return float(1)
            else:
                return float(-1)
        if n == 2:
            return x * x

        flag = False
        if n < 0:
            flag = True
            n = -n

        def power(x, n):
            if n == 1:
                return x
            tmp = x * x
            tmp = power(tmp, n / 2)
            if n % 2 == 1:
                return tmp * x
            return tmp

        res = power(x, n)
        if flag:
            return 1 / res
        return res
