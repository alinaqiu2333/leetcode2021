# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        output_value = self.get_number(l1) + self.get_number(l2)
        head_number = output_value % 10
        ll = ListNode(head_number,None)
        output_value = output_value // 10
        curr = ll
        while output_value != 0 :
            #get the current digit and put it into a node
            curr_number = output_value % 10
            new_node = ListNode(curr_number,None)
            curr.next = new_node
            curr = curr.next
            output_value //= 10
        return ll

    def get_number(self, l):
        temp_n = 0
        multiplier = 1
        while l.next is not None:
            temp_n += multiplier*l.val
            l = l.next
            multiplier *= 10
        temp_n += l.val * multiplier
        return temp_n
