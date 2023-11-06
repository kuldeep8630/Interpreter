class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.token_type == "INTEGER":
            self.eat("INTEGER")
            return Num(token)
        elif token.token_type == "FLOAT":
            self.eat("FLOAT")
            return Num(token)
        elif token.token_type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

    def term(self):
        node = self.factor()
        while self.current_token.token_type in {"MUL", "DIV"}:
            token = self.current_token
            if token.token_type == "MUL":
                self.eat("MUL")
            elif token.token_type == "DIV":
                self.eat("DIV")
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.token_type in {"PLUS", "MINUS"}:
            token = self.current_token
            if token.token_type == "PLUS":
                self.eat("PLUS")
            elif token.token_type == "MINUS":
                self.eat("MINUS")
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def parse(self):
        return self.expr()
class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.token_type == "INTEGER":
            self.eat("INTEGER")
            return Num(token)
        elif token.token_type == "FLOAT":
            self.eat("FLOAT")
            return Num(token)
        elif token.token_type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

    def term(self):
        node = self.factor()
        while self.current_token.token_type in {"MUL", "DIV"}:
            token = self.current_token
            if token.token_type == "MUL":
                self.eat("MUL")
            elif token.token_type == "DIV":
                self.eat("DIV")
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.token_type in {"PLUS", "MINUS"}:
            token = self.current_token
            if token.token_type == "PLUS":
                self.eat("PLUS")
            elif token.token_type == "MINUS":
                self.eat("MINUS")
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def parse(self):
        return self.expr()