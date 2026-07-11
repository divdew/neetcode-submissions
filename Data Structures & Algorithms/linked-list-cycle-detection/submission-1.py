# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        i=head
        j=head.next
        while j and j.next:
            if i==j:
                return True
            i=i.next
            j=j.next.next
        return False