#
# @lc app=leetcode id=28 lang=python
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        needle_length = len(needle)
        for i in range(len(haystack) - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1

# @lc code=end

