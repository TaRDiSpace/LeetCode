class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        # 按字符串长度排序
        strs.sort(key=lambda x: len(x))

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
