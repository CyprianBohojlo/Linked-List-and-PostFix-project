
#The goal of the assignment was to create Linked List and Postfix expression functions and test them on given numbers 

class LList:

    class Node:
        def __init__(self, val, next = None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.nVals = 0

    def addFront(self, val):
        new_node = self.Node(val, self.head)
        self.head = new_node   
        self.nVals += 1

    def getFront(self):
        if self.head is None:
            return None
        else:
            return self.head.val

    def removeFront(self):
            self.head = self.head.next
            self.nVals -= 1
        
    def print(self):
        node = self.head
        while node is not None:
            print( node.val, "--> ", end="")
            node = node.next
        print("*")

    def count(self):
        count, node = 0, self.head
        while node is not None:
            count +=1
            node = node.next 
        return count

    # Function to insert node at given vode used for Postfix
    def insert(self,prev_node,val):
        if prev_node is None:
            print("Node not found to insert node")
            return
        newNode = self.Node(val,self.head)
        prev = self.locate(prev_node)
        # If no node was found
        if prev is None:
            print("No node was found to insert at")
            return
        # If was found
        # set new node next to found node next
        newNode.next = prev.next
        # set next of found node to new node
        prev.next = newNode

    # Function to remove an element with a specific value only one time
    def remove(self, remove_node):
        # Define head node
        headNode = self.head
        # Check if value to delete is head
        if headNode  is not None:
            if headNode.val == remove_node:
                # If value to delete is head, remove and exit
                self.head = headNode.next
                headNode = None
                return
            # Go through list until node to delete is found
            while headNode is not None:
                if headNode.val == remove_node:
                    # If node is found, break
                    break
                # Set previous node to head
                prev = headNode
                # Move head to next node
                headNode = headNode.next
            # if no node to delete was found, exit
            if headNode is None:
                print("Can't find node to delete")
                return
            # If node was found, set the next of previous to next of current node
            prev.next = headNode.next
            headNode = None
    
    def isEmpty(self):
        return self.head == None

    # Prints the list in array format
    def printSLL(self):
        node = self.head
        first = True
        print('[',end='')
        while node is not None:
            if not first:
                print(', ', end="")
            print(node.val, end = "")
            node = node.next
            first = False
        if self.nVals == 0:
               return print('Empty Linked List]')
        print(']')

    # Locates an element in the Singly Linked List 
    def locate(self, i):
        print('')
        found = 'Item was located'
        not_found = 'Item was not located'
        current_node = self.head
        while current_node is not None:
            if current_node.val == i:
                return print(found)
            current_node = current_node.next
        return print(not_found)

    # Function which reverses a linked list
    def reverse(self):
        # Create new empy list to save reversed values
        r_llist = LList()
        # While the list is not empty
        while self.isEmpty() is False:
            # Get first element from list
            first_element = self.getFront()
            # Remove first element from list
            self.removeFront()
            # Add element as first to new list
            r_llist.addFront(first_element)
        return r_llist

#Testing the Linked List function
print('________Singly Linked List TESTING________')
linkedl = LList()
linkedl.printSLL()
linkedl.addFront(5)
linkedl.printSLL()
linkedl.addFront(10)
linkedl.addFront(16)
linkedl.addFront(23)
linkedl.addFront(30)
linkedl.addFront(47)
linkedl.printSLL()

linkedl.locate(0)
linkedl.locate(10)
linkedl.locate(30)
linkedl.locate(341)



class Stack:
    def __init__(self):
        self.llist = LList()

    def push(self, val):
        self.llist.addFront(val)
        
    def pop(self):
        x = self.llist.getFront()
        self.llist.removeFront()
        return x

    def size(self):
        return self.llist.count()

    def peek(self):
        return self.llist.getFront()

# Function to do an operation in the Postfix evaluation
def doOperation(x,y,op):
    if op == '+':
        return float(x)+float(y)
    if op == '-':
        return float(x)-float(y)
    if op == '*':
        return float(x)*float(y)
    if op == '/':
        return float(x)/float(y)

            


# Post evaluation function
def evalPost(e):

    llist = LList()
    last_space = 0
    for i in range(len(e)):
        # Detect white spaces
        if e[i] == " ":
            # If there is a whitespace, parse lastt element, between this and last white space
            element = e[last_space:i]
            last_space = i # Set the new last space to current one
            element = element.replace(" ","") # Remove whitespaces from element
            llist.addFront(element) # Add element to linked list
        if i == len(e)-1: # If the end of the input is reached
            element = e[last_space:i+1] # Parse last element from last white space to end
            element = element.replace(" ","") # Remove whitespaces from element
            llist.addFront(element) # Add element to linked list
    # Reverse Linked list
    llist = llist.reverse()
    # Define new stack only for numbers and results
    num_stack = Stack()
    node = llist.head
    while node is not None:
        if node.val == '*' or node.val == '-' or node.val == '/' or node.val == '+':
            if num_stack.size() < 2:
                print("Error: ",end="")
                num_stack.llist.printSLL()
                return
            op2 = num_stack.pop()
            op1 = num_stack.pop()
            result = doOperation(op1,op2,node.val)
            if result == int(result): # Check if result is a float
                result = int(result)  # If it's not, result shoudl be integer
            num_stack.push(result)
        elif node.val.isdigit():
            num_stack.push(node.val)
        node = node.next
    if num_stack.size() != 1:
        print("Error: ",end="")
        num_stack.llist.printSLL()
        return
    print(num_stack.peek())
    return e

#Testing the postfix function
print('____evalPost TESTING_____')    
evalPost('1')
evalPost('+')
evalPost('1 2 -')
evalPost('1 2 3 4 * - /')
evalPost('1 2 3 4')
evalPost('20 5 - 3 / 2 *')
evalPost('1 -')