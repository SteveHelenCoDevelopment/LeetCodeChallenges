#    Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ll import ListNode



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    # let's walk along the list but swap the links as we go.  Then
    # we can return with the new head of the list when we reach the
    # last node that points to 'None' as the next node:
    # 1->2->3->4->None
    # None<-1..2->3->4->None
    # None<-1<-2..3->4->None
    # None<-1<-2<-3..4->None
    # None<-1<-2<-3<-4          reached end node, return 4 as head node!
        thisNode = head
        nextNode = prevNode = None

        while (thisNode is not None):
            nextNode = thisNode.next
            thisNode.next = prevNode
            prevNode = thisNode
            thisNode = nextNode

        return prevNode


def main():

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    x = head
    y = Solution()
    x = y.reverseList(x)

    while x != None:
        print("{} ->".format(x.val))
        x = x.next


if __name__=="__main__":
    main()      

        
