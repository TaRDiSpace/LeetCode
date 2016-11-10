"""
For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]
You should return the indices: [0,9].
"""


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        res = []
        word = {}
        # 单词个数
        wordNum = len(words)
        # 单词长度
        wordLen = len(words[0])
        # 单词个数字典
        for i in words:
            if i not in word:
                word[i] = 1
            else:
                word[i] += 1
        for i in range(len(s) - wordNum * wordLen + 1):
            tmp = {}
            j = 0
            # 单词未全部组合
            while j < wordNum:
                # 拆分单词
                w = s[i + j * wordLen: i + j * wordLen + wordLen]
                # 如果不存在单词，则跳出循环
                if w not in words:
                    break
                # 如果未见过单词，则记录单词个数
                if w not in tmp:
                    tmp[w] = 1
                # 单词已经出现过，单词个数加一
                else:
                    tmp[w] += 1
                # 出现单词个数大于给出单词个数，则跳出循环
                if tmp[w] > word[w]:
                    break
                j += 1
            # 单词全部组合
            if j == wordNum:
                res.append(i)
        return res
