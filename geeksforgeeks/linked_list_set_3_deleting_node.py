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

    def deleteNode(self, key):
        temp = self.head

        if temp:
            if temp.data == key:
                self.head = temp.next
                return

        prev = None

        while temp:
            if temp.data == key:
                break

            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
