# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = set()
        visited.add(cur)
        while cur.next is not None:
            if cur.next in visited:
                return True
            visited.add(cur.next)
            cur = cur.next
        return False