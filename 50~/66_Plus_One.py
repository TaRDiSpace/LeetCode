class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += flag
            if digits[i] >= 10:
                digits[i] = 0
            else:
                flag = 0
                break
        if i == 0 and flag:
            digits.insert(0, 1)

        return digits
