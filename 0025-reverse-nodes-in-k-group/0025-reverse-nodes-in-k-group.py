# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_range(self, prev, p, q, nodes_count):
        cur = p
        _prev = prev
        next = q.next
        while nodes_count > 0:
            _next = cur.next
            cur.next = _prev
            _prev = cur
            cur = _next
            nodes_count -= 1
        
        prev.next = _prev
        p.next = cur
        
        return cur
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        
        b = ListNode(None)
        b.next = head
        
        prev = b
        cur = head
        
        while cur:
            p = cur
            for i in range(k-1):
                if not cur or not cur.next: return b.next
                cur = cur.next
            q = cur
            
            cur = self.reverse_range(prev, p, q, k)
            prev = p
            
        return b.next
                
            