class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1
        length1 = len(num1)
        length2 = len(num2)
        if length1 == 1 and length2 == 1:
            return str(int(num1) * int(num2))

        res = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        nums = [0 for i in range(length1 + length2)]

        # 算出从右往左的所有数
        for i in range(length1):
            for j in range(length2):
                nums[i + j] += int(num1[i]) * int(num2[j])

        # 将数字个位插入列表第一位，进位加向下一位
        for i in range(len(nums)):
            num = nums[i] % 10
            c = nums[i] // 10
            if i < len(nums) - 1:
                nums[i + 1] += c
            res.insert(0, str(num))
        # 去除结果前面的0
        while res[0] == '0':
            del res[0]

        return ''.join(res)
