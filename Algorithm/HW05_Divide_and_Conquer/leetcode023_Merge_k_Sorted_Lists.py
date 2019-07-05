# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/


# Runtime: 88 ms
# Memory Usage: 16.4 MB
# Your runtime beats 60.70 % of python3 submissions.
# Your memory usage beats 64.28 % of python3 submissions.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        
        return self.merge(lists, 0, len(lists)-1)
    
    def merge(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        s1 = self.merge(lists, start, mid)
        s2 = self.merge(lists, mid + 1, end)
        
        if not s1: return s2
        if not s2: return s1
        
        node = ListNode(0)
        if s1.val <= s2.val:
            node = s1
            s1 = s1.next
        else:
            node = s2
            s2 = s2.next
            
        root = node
            
        while s1 and s2:
            if s1.val <= s2.val:
                node.next = s1
                s1 = s1.next
            else:
                node.next = s2
                s2 = s2.next
            node = node.next
        
        while s1:
            node.next = s1
            node = node.next
            s1 = s1.next
            
        while s2:
            node.next = s2
            node = node.next
            s2 = s2.next
            
        return root