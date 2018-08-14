# Implementing Stack using Linked Lists

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.start=None
        self.enterchoice()

    def push(self, data):
        if self.empty():
            self.start=Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.start
            self.start = newNode

    def pop(self):
        if self.empty():
            print('Stack is empty!')
        else:
            popped=self.start.data
            self.start=self.start.next
            return popped

    def display(self):
        while not self.empty():
            print(self.start.data)
            self.start=self.start.next
        else:
            print('Stack is empty')

    def empty(self):
        if self.start is None: return True
        else: return False

    def top(self):
        print(self.start.data)

    def enterchoice(self):
        while True:
            print('Choice:\n1: Push\n2: Pop\n3: Display\n4: Exit\n5: Top')
            self.choice = int(input('Enter your choice: '))
            if self.choice == 1:
                data = int(input('Enter value: '))
                self.push(data)
            if self.choice == 2:
                self.pop()
            if self.choice == 3:
                self.display()
            if self.choice == 4:
                exit(0)
            if self.choice==5:
                self.top()
            if self.choice not in [1, 2, 3, 4,5]:
                print('Wrong choice try again!')
                continue
