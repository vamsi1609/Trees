"""
This module implements linked list 
"""

class Node():
    """
    Node class holds the data and the next node
    """
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    
    def insertAtStart(self, data):
        """
        Insert data to the start of the linked list

        Args:
            data (any): data to be inserted 
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertAtIndex(self, data, index):
        """
        Method to insert data to a specific location

        Args:
            data (any): data to be inserted
            index (int): index at which the data needs to be inserted 
        """
        if index ==0:
            self.insertAtStart(data)
            return

        position = 0
        current_node = self.head
        # traverse through the list 
        while(current_node is not None and position+1!=index):
            position+=1
            current_node = current_node.next
        
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("index not available")
    
    
    def update_node(self, data, index):
        current_node = self.head
        position= 0 
        while current_node is not None and position!=index:
            position+=1
            current_node = current_node.next
        
        if current_node is not None:
            current_node.data = data
        else:
            print("Index not found!!!")
    
    
    def removeAtStart(self):
        if self.next is None:
            return None
        self.head = self.head.next
        
        
            
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = '->')
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtStart(4)
    ll.insertAtStart(10)
    ll.insertAtStart(15)
    ll.insertAtIndex(2,2)
    ll.traverse()
    ll.insertAtIndex(9,5)
    ll.insertAtStart(666)
    ll.insertAtIndex(9,5)
    ll.traverse()
    
    
        
        
        
        