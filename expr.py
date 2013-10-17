from copy import deepcopy


class BinaryTree():

    def __init__(self, value):
        self.lnode = None
        self.rnode = None
        self.value = value

    def __len__(self):
        if not(self.lnode and self.rnode):
            return 1
        nLeft = self.lnode.__len__()
        nRight = self.rnode.__len__()
        if nLeft > nRight:
            return nLeft + 1
        else:
            return nRight + 1

    def full(self, depth):
        if depth != 1:
            if self.lnode == None:
                self.lnode = BinaryTree(" ")
            if self.rnode == None:
                self.rnode = BinaryTree(" ")
            self.lnode.full(depth - 1)
            self.rnode.full(depth - 1)

    def __repr__(self):
        output = ''
        t = deepcopy(self)
        t.full(len(t) + 1)  # to make it look better, add a layer

        def add_space(node):  # the rule of adding spaces to nodes
            if not(node.lnode or node.rnode):
                node.value = ' ' + node.value + ' '
            else:
                length = len(node.lnode.value) + len(node.rnode.value)
                if length % 2 == 0:
                    node.value = ' ' * \
                        (length // 2 - 1) + node.value + ' ' * (length // 2)
                else:
                    node.value = ' ' * \
                        (length // 2) + node.value + ' ' * (length // 2)

        def add(node):  # add spaces (postorder-traversal)
            if node.lnode or node.rnode:
                add(node.lnode)
                add(node.rnode)
            add_space(node)

        add(t)
        quene = [t]
        i = 0
        while i < len(quene):
            last = len(quene)
            while i < last:
                output += quene[i].value
                if quene[i].lnode:
                    quene.append(quene[i].lnode)
                if quene[i].rnode:
                    quene.append(quene[i].rnode)
                i += 1
            output += '\n\n'
        return output[:-1]

    def eval(self):

        def calculate(a, b, op):
            operator = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
                        '*': lambda a, b: a * b, '/': lambda a, b: a / b}
            assert op in operator
            return operator[op](a, b)

        if not(self.lnode or self.rnode):
            return self.value
        else:
            num1 = self.lnode.eval()
            num2 = self.rnode.eval()
            return calculate(int(num1), int(num2), self.value)

    def postorder(self):
        if self.lnode and self.rnode:
            output = str(self.value)
            left = self.lnode.postorder()
            right = self.rnode.postorder()
            return left + right + output
        else:
            return str(self.value)


def infix_to_postfix(expr):
    assert isinstance(expr, str)
    output = []
    stack = []
    operator = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': -2}
    for i in expr:
        if i not in operator:
            output.append(i)
        else:
            if operator[i] == -1:
                stack.append(i)
            elif operator[i] == -2:
                while operator[stack[-1]] != -1:
                    output.append(stack.pop())
                stack.pop()
            elif stack == [] or operator[stack[-1]] < operator[i]:
                stack.append(i)
            else:
                while len(stack) != 0 and operator[stack[-1]] >= operator[i]:
                    output.append(stack.pop())
                stack.append(i)
    output.extend(stack[::-1])
    return "".join(output)


def postfix_to_exprtree(expr):
    stack = []
    operator = ['+', '-', '*', '/']
    for i in expr:
        if i not in operator:
            stack.append(BinaryTree(i))
        else:
            t = BinaryTree(i)
            num1 = stack.pop()
            num2 = stack.pop()
            t.lnode, t.rnode = (num2, num1)
            stack.append(t)
    return stack[0]


def verticalprint(tree):
    def _printtree(tree, layer):
        if tree:
            _printtree(tree.rnode, layer + 3)
            print(' ' * layer, end="")
            print(tree.value)
            _printtree(tree.lnode, layer + 3)
    _printtree(tree, len(tree))