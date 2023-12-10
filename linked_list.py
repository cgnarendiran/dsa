class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node data is {self.data}"


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, insert_index, data):
        insert_node = Node(data=data)

        # Insertion at the head
        if insert_index == 0:
            insert_node.next_node = self.head
            self.head = insert_node
            return

        current = self.head
        current_index = 0

        while current is not None:
            if current_index + 1 == insert_index:
                insert_node.next_node = current.next_node
                current.next_node = insert_node
                return
            current = current.next_node
            current_index += 1

    def search(self, data):
        if self.head is None:
            return None

        current = self.head
        current_index = 0

        while current is not None:
            if current.data == data:
                return current_index
            current = current.next_node
            current_index += 1

        return None


N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(40)

N1.next_node = N2
N2.next_node = N3
N3.next_node = N4

L1 = LinkedList(N1)
