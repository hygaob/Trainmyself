#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
    
# @lc code=end
# q=input("請輸入整數陣列(以空格分隔):")
# val=int(input("請輸入要移除的元素:"))
# nums=list(map(int,q.split()))
# print(Solution().removeElement(nums,val))
