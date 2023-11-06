

class Node:
    pass

class Program(Node):
    def __init__(self):
        self.statements = []

class BinaryExpression(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Literal(Node):
    def __init__(self, value):
        self.value = value