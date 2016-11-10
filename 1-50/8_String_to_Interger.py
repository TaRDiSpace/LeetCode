class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        count, sign, i = 0, 1, 0
        if str == '':
            return 0
        # 跳过前面空格
        while i < len(str) and str[i].isspace():
            i += 1
        # 判断符号
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        # 当字符是数字
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            # 先前数字进位
            if count * 10 <= INT_MAX:
                count *= 10
            # 越界
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            # 累加新的数字
            if count + digit <= INT_MAX:
                count += digit
            # 越界
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign * count
