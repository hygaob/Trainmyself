#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode(0)
        current=list3
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next=list1 if list1 else list2
        return list3.next

# @lc code=end
input1=input("請輸入第一個已排序的鏈結串列(以空格分隔):")
input2=input("請輸入第二個已排序的鏈結串列(以空格分隔):")
list1_vals = list(map(int, input1.split()))
list2_vals = list(map(int, input2.split()))
def create_linked_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

list1 = create_linked_list(list1_vals)
list2 = create_linked_list(list2_vals)