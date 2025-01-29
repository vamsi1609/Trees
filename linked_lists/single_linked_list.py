"""
This module implements single linked list
"""

class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class SingleLinkedList():
    def __init__(self) -> None:
        self._head = None
    def insertAtStart(self, data) -> None:
        if self._head == None:
            self._head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
    
    def traverse(self) -> None:
        
        current_node = self._head
        while(current_node):
            
            print(current_node.data,end="->")  
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    list = SingleLinkedList()
    list.insertAtStart(5)
    list.insertAtStart(3)
    list.insertAtStart(10)
    list.traverse()