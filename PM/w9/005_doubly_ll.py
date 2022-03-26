class Node:
    def __init__(self, data = 0, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_LL:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def insert_node(self, data):
        if not self.head and not self.tail:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_node(self, data):
        tmp = self.head
        while tmp is not None and tmp.data != data:
            tmp = tmp.next
        if tmp is None:
            return
        
        if tmp == self.head:
            tmp_node = self.head.next
            if tmp_node:
                tmp_node.prev = None
            if self.tail == self.head:
                self.tail = tmp_node
            del self.head
            self.head = tmp_node
        else:
            if tmp.next:
                tmp.next.prev = tmp.prev
            if tmp.prev:
                tmp.prev.next = tmp.next
            if tmp == self.tail:
                self.tail = tmp.prev
            del tmp
    
    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


my_list = Doubly_LL()
for itm in input("Enter elements to insert seperated by space = ").split(" "):
    my_list.insert_node(int(itm))
print("The list is")
my_list.print_list()

for itm in input("Enter elements to delete seperated by space = ").split(" "):
    my_list.delete_node(int(itm))
print("The list is")
my_list.print_list()
