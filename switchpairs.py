# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
      
def swapPairs(head):

    print("here and head.val is {} and head.next is {}".format(head.val,head.next))
    if head == None:
        # if next node is empty then do nothing
        return head
    if head.next == None:
        # if only one node beyond this one, then do nothing (you need a pair to swap order!!!!)
        return head
    if head.next.next != None:
        # if this is NOT the last pair, then go to the next pair and try to switch them!
        head.next.next = swapPairs(head.next.next)  # the new head is 2 positions along the unchanged list

    head, head.next, head.next.next= head.next, head, head.next.next  #(y->1->2->3 goes to y->2->3)
    return head # we need this in order to be able to link to this node from the calling routine

        
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next.next.next = ListNode(8)

    x = head

    x = swapPairs(x)


    while x != None:
        print("{} ->".format(x.val))
        x = x.next

 
if __name__=="__main__":
    main()
