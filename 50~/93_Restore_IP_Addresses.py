"""
For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 4:
            return [s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3]]

        def rec(s, part, res, ip):
            if part == 4:
                if not s:
                    res.append(ip[1:])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        rec(s[i:], part + 1, res, ip + '.' + s[:i])
                    if s[0] == '0':
                        break

        res = []
        rec(s, 0, res, '')
        return res
