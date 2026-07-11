# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return 
        def reverseLL(x:Optional[ListNode]):
            t=None
            c=x
            while c!=None:
                n=c.next
                c.next=t
                t=c
                c=n
            return t
        
        o=head
        t=head.next
        while t!=None and t.next!=None:
            o=o.next
            t=t.next.next
        t=o.next
        o.next=None
        o=reverseLL(t)
        t=head
        while o!=None and t!=None:
            n=t.next
            m=o.next
            t.next=o
            o.next=n
            o=m
            t=n
        return 