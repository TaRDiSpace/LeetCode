"""
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        l = 0
        dic = {}

        for i, ch in enumerate(s):
            # 如果出现重复字符，则从前字符上一个位置的下一位开始计算
            if ch in dic and dic[ch] >= l:
                l = dic[ch] + 1
            # 更新字符位置
            dic[ch] = i
            # 对比当前长度与计算长度
            res = max(res, i - l + 1)
        return res
