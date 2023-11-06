from my_parser import BinOp
from my_parser import Num

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        if isinstance(node, BinOp):
            if node.op.token_type == "PLUS":
                return self.visit(node.left) + self.visit(node.right)
            elif node.op.token_type == "MINUS":
                return self.visit(node.left) - self.visit(node.right)
            elif node.op.token_type == "MUL":
                return self.visit(node.left) * self.visit(node.right)
            elif node.op.token_type == "DIV":
                return self.visit(node.left) / self.visit(node.right)
        elif isinstance(node, Num):
            return node.value

    def interpret(self):
        tree = self.parser.parse()
        if tree is None:
            return ""
        return self.visit(tree)