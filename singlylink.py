class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return

    def traverse_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def is_empty(self):
        return self.head is None


my_list = SinglyLinkedList()

my_list.insert_at_end(1)
my_list.insert_at_beginning(2)
my_list.insert_at_end(3)

print("After insertions:")
my_list.traverse_list()  # Output: 2 1 3

my_list.delete_node(1)
print("\nAfter deleting 1:")
my_list.traverse_list()  # Output: 2 3

if my_list.is_empty():
    print("\nList is empty.")
else:
    print("\nList is not empty.")