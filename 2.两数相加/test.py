## Firstly, a definition for singly-linked list is already given.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = next





## Then, the function to add two numbers is implemented.

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # construct a new linked list to store the result
    # to find the head of the linked list, a dummy node is created
    dummy = ListNode(0)
    # current node point to dummy node
    current = dummy
    # initialize carry to 0
    carry = 0
    # while the two input linked lists are not empty or carry is not 0
    while l1 or l2 or carry:
        # sum up the values of the two nodes and the carry
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        # creating a new node to store the sum

        ## Note: the current node must be updated to the next node.
        current.next = listNode(sum % 10)
        # update the carry
        carry = sum // 10
        # move to the next node
        current = current.next
        if l1:
            l1 = l1.next
        if l2: 
            l2 = l2.next
    return dummy.next