# Implementing Stack using Arrays

class Stack:
    def __init__(self):
        self.stack = []
        self.enterchoice()

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def display(self):
        for i in reversed(self.stack):
            print(i)

    def empty(self):
        return self.stack==[]

    def size(self):
        return len(self.stack)

    def top(self):
        print(reversed(self.stack[0]))

    def enterchoice(self):
        self.empty()
        while True:
            print('Choice:\n1: Push\n2: Pop\n3: Display\n4: Exit\n5: Top')
            self.choice = int(input('Enter your choice: '))
            if self.choice == 1:
                if self.size()>=500:
                    print('Stack is full!')
                    continue
                else:
                    val = int(input('Enter value: '))
                    self.push(val)
            if self.choice == 2:
                if self.empty():
                    print('Stack is empty!')
                    continue
                else:
                    self.pop()
            if self.choice == 3:
                if self.empty():
                    print('Stack is empty!')
                    continue
                else:
                    self.display()
            if self.choice == 4:
                exit(0)
            if self.choice==5:
                self.top()
            if self.choice not in [1,2,3,4]:
                print('Wrong choice try again!')
                continue
                
