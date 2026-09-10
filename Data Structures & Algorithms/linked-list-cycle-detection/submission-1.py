# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        seen = set()

        currentNode = head

        while currentNode:
            if currentNode in seen:
                return True
            seen.add(currentNode)
            currentNode = currentNode.next
        return False