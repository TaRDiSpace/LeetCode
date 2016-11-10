"""
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def rec(l, target, p, tmp):
            if target == 0:
                res.append(tmp)
                return
            for i in range(p, len(l)):
                if target < l[i]:
                    return
                else:
                    rec(l, target - l[i], i, tmp + [l[i]])

        tmp = []
        res = []
        candidates.sort()
        rec(candidates, target, 0, tmp)
        return res
