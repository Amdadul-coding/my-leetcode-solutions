# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        temp = head
        temp2 = head.next
        last = head.val
        while temp2:
            if temp2.val == last:
                if not temp2.next:
                    temp.next = None
                    break
                temp2 = temp2.next
                temp.next = temp2
            else:
                temp = temp2
                last = temp.val
                temp2 = temp2.next
        return head
