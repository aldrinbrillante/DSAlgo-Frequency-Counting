from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def find(self,item):
    current = self.head
    found = False

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next

    if found:
      current.data = (current.data[0], (current.data[1] + 1))
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter += 1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'{current.data}')
        current = current.next
