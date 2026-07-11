# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        ans=ListNode(None)
        t=ans
        while p1!=None and p2!=None:
            if p1.val<=p2.val:
                t.next=p1
                t=t.next
                p1=p1.next
            else:
                t.next=p2
                t=t.next
                p2=p2.next
        while p1!=None:
            t.next=p1
            t=t.next
            p1=p1.next
        while p2!=None:
            t.next=p2
            t=t.next
            p2=p2.next
        return ans.next