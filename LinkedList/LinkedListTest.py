class Node:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.data, end = ' ')
            tempNode = tempNode.next
        #This statment is used to insert a new line after the result
        print()

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.printList()
