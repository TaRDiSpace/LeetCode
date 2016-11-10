"""
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""


class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 2:
            return 0
        if nums[0] >= length:
            return 1

        res = 0
        last = 0
        dist = 0
        for i in range(length):
            # 如果当前位置大于能跳到的最大距离，跳数加一
            if i > last:
                last = dist
                res += 1
            # 当前位置可以跳到的最大距离
            dist = max(dist, i + nums[i])
            if dist >= length - 1:
                res += 1
                return res

        return res
