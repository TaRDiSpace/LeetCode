"""
a + b + c = 0 ?
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length, res = len(nums), []
        if length < 3:
            return []
        nums.sort()
        for i in range(length - 2):
            j = i + 1
            k = length - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return res
