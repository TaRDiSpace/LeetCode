"""
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        length, res, dic = len(nums), set(), {}
        if length < 4:
            return []
        nums.sort()
        # 将a+b的所有结果记录在字典中
        for p in range(length):
            for q in range(p + 1, length):
                if nums[p] + nums[q] not in dic:
                    dic[nums[p] + nums[q]] = [(p, q)]
                else:
                    dic[nums[p] + nums[q]].append((p, q))
        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                tmp = target - nums[i] - nums[j]
                # 如果剩余两个数相加结果在字典中
                if tmp in dic:
                    for k in dic[tmp]:
                        # 如果下一个数在第二个数之后，则记录结果
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]
