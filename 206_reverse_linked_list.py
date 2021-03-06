# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None 
        next = None 
        while head:
            next = head.next 
            head.next = prev 
            prev = head
            head = next
        return prev
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None,head
        while cur:
            cur.next,pre,cur=pre,cur, cur.next
        return pre

