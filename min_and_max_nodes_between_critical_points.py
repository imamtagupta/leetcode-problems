#############################################
# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points                #
#############################################

# leetcode link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ls = []
        i = 1
        curr, prev= head.next, head
        if curr.next:
            lat = curr.next
        else:
            return [-1, -1]
        while curr and curr.next:
            print(prev.val, curr.val, lat.val)
            if curr.val > prev.val and curr.val > lat.val:
                ls.append(i)
            if curr.val < prev.val and curr.val < lat.val:
                ls.append(i)
            prev = curr
            curr = curr.next
            lat = lat.next
            i += 1
        if len(ls) < 2:
            return [-1, -1]

        n = len(ls)-1
        min_yet = 1000000000
        for i in range(n):
            if min_yet > (ls[i+1] - ls[i]):
                min_yet = ls[i+1] - ls[i]
        return [min_yet, ls[n]-ls[0]]