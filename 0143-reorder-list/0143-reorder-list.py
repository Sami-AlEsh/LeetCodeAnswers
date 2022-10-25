# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, node):
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        return prev_node
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Cut the list into 2 halves
        l1 = head
        # Reverse the second half of the linked list
        l2 = self.reverse_linked_list(slow)

        # Merge 2 lists together
        while l1 and l2:
            temp = l1.next
            l1.next = l2
            l1 = temp

            temp = l2.next
            l2.next = l1
            l2 = temp

        # set the next of the last node to 'None'
        if l1 is not None:
            l1.next = None