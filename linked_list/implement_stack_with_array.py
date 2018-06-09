class Stack():
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack)-1]

    ( def) pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return None

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    
    def __repr__(self):
        return str(self.stack)
        

s = Stack()
s.push('s')
s.push('t')
s.push('a')
s.push('z')
assert s.stack == ['s', 't', 'a', 'z']
assert s.peek() == 'z'
s.pop()
assert s.stack == ['s', 't', 'a']
assert s.is_empty() == False
s.pop()
s.pop()
print(s.peek())
assert s.peek() == 's'
s.pop()
s.pop()
s.pop()
assert s.is_empty() == True
print (s)
