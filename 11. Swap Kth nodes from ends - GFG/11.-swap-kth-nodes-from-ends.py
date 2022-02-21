#User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
#Function to swap Kth node from beginning and end in a linked list.
def swapkthnode(head,num,k):
    
    if k>num:
        return head
        
    if (2*k -1) == num:
        return head
    
    t1 = head
    t2 = head
    prev1 = None
    prev2 = None
    
    for i in range(k-1):
        prev1 = t1
        t1 = t1.next
        
    for i in range(num - k):
        prev2 = t2
        t2 = t2.next
        
    
    
    if prev1 is not None:
            prev1.next = t2

    if prev2 is not None:
        prev2.next = t1
    
    
    temp = t1.next
    t1.next = t2.next
    t2.next = temp
    
    if k == 1:
        head = t2
        
    if k == num:
        head = t1
    
    
    return head

        
        
        
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head=swapkthnode(a.head,n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends