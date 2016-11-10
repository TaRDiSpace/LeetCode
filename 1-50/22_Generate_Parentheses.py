"""
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret = []
        res = ''

        def recursion(l, r, n, res):
            # 如果右括号有n个，则完成配对
            if r == n:
                ret.append(res)
                return
            # 如果右括号等于左括号，则下一个为左括号
            if r == l:
                res += '('
                l += 1
                recursion(l, r, n, res)
            # 左括号大于右括号
            else:
                # 左括号有n个，则下一个为右括号
                if l == n:
                    res += ')'
                    r += 1
                    recursion(l, r, n, res)
                # 左括号没放完，下一个要么左括号要么右括号
                else:
                    # 下一个放左括号
                    res += '('
                    l += 1
                    recursion(l, r, n, res)
                    res = res[:-1]
                    l -= 1
                    # 下一个放右括号
                    res += ')'
                    r += 1
                    recursion(l, r, n, res)

        recursion(0, 0, n, res)
        return ret
