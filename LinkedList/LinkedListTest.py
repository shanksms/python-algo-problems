class Node:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    #def __init__(self):
    #    self.head = None
    def printList(self, node):
        while node:
            print(node.data, end = ' ')
            node = node.next
        #This statment is used to insert a new line after the result
        print()

    def mergeLinkedLists(self, node1, node2):
        head = tail = Node()
        while node1 and node2:
            if node1.data < node2.data:
                tail.next, node1 = node1, node1.next
            else:
                tail.next, node2 = node2, node2.next
            tail = tail.next

        if node1 is None:
            tail.next = node2
        else:
            tail.next = node1
        return head.next
    def detectCycle1(self, node):
        s = set()
        s.add(node)
        while node:
            if node.next in s:
                #Calculate cycle length
                return self.cycleLength(node.next)
            else:
                s.add(node.next)
            node = node.next
        return None
    def detectCycle2(self, node):
        slow = node.next
        #if there is only one node, then return None
        if slow == None:
            return None
        fast = node.next.next
        while slow and fast  and fast.next:
            if slow is fast:
                #loop exists
                return self.cycleLength(slow)
            else:
                slow = slow.next
                fast = fast.next.next
        return None
    def length(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    def overlapping_nocycle_lists(self, node1, node2):
        len1, len2 = self.length(node1), self.length(node2)
        if len1 > len2:
            #make node2 longer one always. it will simplify the code
            node2, node1 = node2, node1
        for _ in range(abs(len1 - len2)):
            node2 = node2.next
        while node1 and node2 and node1 is not node2:
            node1, node2 = node1.next, node2.next
        return node1

    def cycleLength(self, node):
        tmpNode = node.next
        step = 1
        while tmpNode is not node:
            step += 1
            tmpNode = tmpNode.next

        return step

def test_length():
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    first.next = second
    second.next = third
    print(llist.length(first))

def testPrintList():
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    first.next = second
    second.next = third
    llist.printList(first)

def testMergeLists():
    llist = LinkedList()
    first1 = Node(1)
    second1 = Node(4)
    third1 = Node(7)
    first1.next = second1
    second1.next = third1

    first2 = Node(2)
    second2 = Node(3)
    third2 = Node(9)
    first2.next = second2
    second2.next = third2

    result = llist.mergeLinkedLists(first1, first2)
    llist.printList(result)
def testCycle():
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    first.next = second
    second.next = third
    third.next = first
    print(llist.detectCycle2(first))
def test_overlapping_nocycle_lists():
    llist = LinkedList()
    first1 = Node(1)
    second1 = Node(4)
    third1 = Node(8)
    first1.next = second1
    second1.next = third1

    first2 = Node(2)
    second2 = Node(3)

    first2.next = second2
    second2.next = third1
    start_common_node = llist.overlapping_nocycle_lists(first1, first2)
    llist.printList(start_common_node)
if __name__ == '__main__':
    test_overlapping_nocycle_lists()
