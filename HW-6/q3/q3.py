class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
        def __init__(self, head=None):
            self.head = head

        def print_list(self):
            if self.head == None:
                raise ValueError("List is empty")

            current = self.head
            while current:
                print(current.data, end="  ")
                current = current.next
            print("\n")

        # Find length of Linked List
        def size(self):
            if self.head == None:
                return 0

            size = 0
            current = self.head
            while current:
                size += 1
                current = current.next

            return size

        # Insert a node in a linked list
        def insert(self, data):
            node = Node(data)
            current = self.head
            if not current:
                self.head = node
            else:
                while (current.next):
                    current = current.next
                current.next = node
        def insert_beginning(self, data):
            node = Node(data)
            current = self.head
            self.head = node
            node.next = current

        # Delete a node in a linked list
        def delete(self, data):
            if not self.head:
                return

            temp = self.head

            # Check if head node is to be deleted
            if self.head.data == data:
                head = temp.next
                print("Deleted node is " + str(self.head.data))
                return

            while temp.next:
                if temp.next.data == data:
                    print("Node deleted is " + str(temp.next.data))
                    temp.next = temp.next.next
                    return
                temp = temp.next
            print("Node not found")
            return

        def sort(self):
            i = self.head
            while i is not None:
                min_val = i  # compare with each element to change the min
                next_val = i.next
                
                #Find the minimum element in remaining
                while next_val is not None:
                    if min_val.data > next_val.data:
                        min_val = next_val
                    next_val = next_val.next
                
                # Swap the found minimum element withthe first element  
                swap = i.data
                i.data = min_val.data
                min_val.data = swap
                i = i.next

# test case
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
print("The Linked List is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()

