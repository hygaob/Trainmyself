#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=x
        rev_num=0
        while y>0:
            rev_num=rev_num*10+y%10
            y//=10
        return rev_num==x
# @lc code=end
x=int(input())
sol = Solution()
print(sol.isPalindrome(x))