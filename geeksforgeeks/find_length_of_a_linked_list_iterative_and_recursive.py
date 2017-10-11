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

    def getCount(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def getCountRec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next)


if __name__ == '__main__':
    list = LinkedList()
    list.push(1)
    list.push(3)
    list.push(1)
    list.push(2)
    list.push(1)

    print('The count of nodes is: ', list.getCount())
    print('The count of nodes is: ', list.getCountRec(list.head))
