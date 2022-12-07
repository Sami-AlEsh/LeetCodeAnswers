# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def circular_list_count(self, node):
        cnt = 1
        head = node
        while node.next:
            node = node.next
            cnt += 1
        node.next = head
        return cnt
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head
        
        length = self.circular_list_count(head)
        k = k % length
        
        if length == 1:
            head.next = None
            return head
        
        skip = length - k
        while skip > 0:
            prev = head
            head = head.next
            skip -= 1
        prev.next = None
        return head