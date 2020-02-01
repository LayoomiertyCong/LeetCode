#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p=l1
        q=l2
        carry=0
        first_flag=1
        head=None
        c_node=None
        while p!=None or q!=None or carry!=0:
            val1=0
            val2=0
            if p!=None:
                val1=p.val
                p=p.next
            if q!=None:
                val2=q.val
                q=q.next
            temp_sum=val1+val2+carry
            if temp_sum>=10:
                carry=1
                temp_sum=temp_sum%10
            else:
                carry=0
            temp_node=ListNode(temp_sum)
            if first_flag==1:
                c_node=temp_node
                head=temp_node
                first_flag=0
            else:
                c_node.next=temp_node
                c_node=c_node.next
        return head

