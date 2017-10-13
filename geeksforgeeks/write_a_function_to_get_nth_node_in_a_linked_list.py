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


if __name__ == '__main__':
    pass
