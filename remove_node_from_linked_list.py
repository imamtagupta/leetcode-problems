
########################################
# 2487. Remove Nodes From Linked List  #
########################################

# leetcode link: https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev, curr, nxt = None, head, head.next
        while curr is not None:
            curr.next = prev
            prev, curr = curr, nxt
            nxt = nxt.next if nxt else None
        return prev

    def remove_right_mins(self, head, nmax):
        if not head and not head.next :
            return head
        curr = head
        while curr.next is not None:
            if curr.next.val < nmax:
                temp = curr.next
                curr.next = curr.next.next
                temp = None
            else:
                nmax = curr.next.val
                curr = curr.next
        return head



    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        revHead = self.reverse(head)
        self.remove_right_mins(revHead, revHead.val)
        return self.reverse(revHead)
        

        