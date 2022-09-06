class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.top=None

class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    new=Node(data)
    new.data=data
    new.next=self.top
    self.top=new
  def pop(self) -> None:
    # Write your code here
    if self.top==None:
      return None
    else:
      #temp=Node(data)
      temp=self.top
      return temp
      self.top=self.top.next
      
  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    if self.top==None:
      print("None")
    else:
      #ptr=Node(data)
      ptr=self.top
      while(ptr!=None):
        print(ptr,"=>",end="")
        ptr=ptr.next
      else:
        print("None")
# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
