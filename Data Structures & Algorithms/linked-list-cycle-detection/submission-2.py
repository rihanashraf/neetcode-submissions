# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dicti = {}

        curr = head
        while curr:
            if curr not in dicti:
                dicti[curr] = 1
            else:
                return True
            curr = curr.next
        
        return False

        #O(n) space complexity and O(n) time complexity


        