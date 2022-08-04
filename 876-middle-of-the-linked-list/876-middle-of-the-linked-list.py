# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        try:
            while fast != None:
                slow = slow.next
                fast = fast.next.next
            return slow
        except:
            return slow
            
        
        
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next
        
        cc = count // 2
        if count % 2 == 0:
            cc += 1
        
        cur = head
        for _ in range(cc):
            cur = cur.next
        
        return cur.val
            
        