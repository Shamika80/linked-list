class Node:
    
     def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
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
            new_node.prev = current

    def delete_by_value(self, data):
        
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:  
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                elif current.next is None:  
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def traverse_forward(self):
        
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        
        current = self.head
        if current is not None:
            while current.next is not None:
                current = current.next
            while current is not None:
                print(current.data, end=" ")
                current = current.prev
        print()

my_list = DoublyLinkedList()

my_list.insert_at_beginning(5)
my_list.insert_at_beginning(10)
my_list.insert_at_beginning(15)

print("List after inserting at beginning:")
my_list.traverse_forward()  

my_list.insert_at_end(20)
my_list.insert_at_end(25)

print("List after inserting at end:")
my_list.traverse_forward()  

my_list.delete_by_value(10)
my_list.delete_by_value(25)

print("List after deleting by value:")
my_list.traverse_forward()  

print("Traversing forward:")
my_list.traverse_forward()  

print("Traversing backward:")
my_list.traverse_backward()  

my_list.delete_by_value(30)

if my_list.head is None:
    print("The list is empty")
else:
    print("The list is not empty")  