# use dict
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l = {}
        while headA:
            l[headA] = 1
            headA = headA.next
        while headB:
            if headB in l:
                return headB
            headB = headB.next
        print l
