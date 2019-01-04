#1. Linked Lists and Stacks
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        self.top = self.top.next

    def peek(self):
        return self.top.data

    def is_empty(self):
        return True if self.top is None else False


# NO modifications below this line
import sys

complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)

#2. Balanced Parentheses
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

def is_paren_balanced(symbol_str):
    s = Stack()
    is_balanced = True
    i = 0
    while i < len(symbol_str) and is_balanced:
        symbol = symbol_str[i]
        if symbol in "([{<":
            s.push(symbol)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    is_balanced = False
        i = i + 1
    if is_balanced and s.is_empty():
        return True
    else:
        return False

def matches(op, close):
    opens = "([{<"
    closes = ")]}>"
    return opens.index(op) == closes.index(close)

s = input()
print(is_paren_balanced(s))

#3. Doubly Linked Lists and Queue
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, x):
        newNode = Node(x)
        newNode.next = None
        if self.front == None:
            self.front = newNode
            self.back = newNode
        else:
            self.back.next = newNode
            newNode.previous = self.back
            self.back = newNode

    def dequeue(self):
        item = self.front.data
        self.front = self.front.next
        return item

    def is_empty(self):
        return self.front == None


# NO modifications below this line
import sys

complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)
