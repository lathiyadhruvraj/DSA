class Stack:
    # Not any in-built python class available for STACK
    # Implementing Stack using List

    def __init__(self, initVal:list = []):
        self.stack = initVal

    def add(self, item):
        if type(item) == list:
            self.stack.extend(item)
        else:
            self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        if self.stack is None:
            return 'Empty Stack'
        else:
            return repr(self.stack)

st1 = Stack()
st1.add(1)
st1.add([2, 3, 5, 6])
st1.pop()
print(st1)
