class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def swapNodes(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head

        while currX is not None and currX.data != x:
            prevX = currX
            currX = currX.next


if __name__ == '__main__':
    pass
