
########################################
# 2816. Double a Number Represented as a Linked List  #
########################################

# leetcode link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.val >= 5:
      head = ListNode(0, head)

    curr = head

    while curr:
      curr.val *= 2
      curr.val %= 10
      if curr.next and curr.next.val >= 5:
        curr.val += 1
      curr = curr.next

    return head

        