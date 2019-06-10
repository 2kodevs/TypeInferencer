import cmp.visitor as visitor
from cmp.CoolUtils import *

#AST Printer
class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__ProgramNode [<class> ... <class>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.declarations)
        return f'{ans}\n{statements}'
    
    @visitor.when(ClassDeclarationNode)
    def visit(self, node, tabs=0):
        parent = '' if node.parent is None else f"inherits {node.parent}"
        ans = '\t' * tabs + f'\\__ClassDeclarationNode: class {node.id} {parent} {{ <feature> ... <feature> }}'
        features = '\n'.join(self.visit(child, tabs + 1) for child in node.features)
        return f'{ans}\n{features}'
    
    @visitor.when(AttrDeclarationNode)
    def visit(self, node, tabs=0):
        sons = [node.expr] if node.expr else []
        text = '<- <expr>' if node.expr else ''
        ans = '\t' * tabs + f'\\__AttrDeclarationNode: {node.id} : {node.type} {text}'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}' if body else f'{ans}'
    
    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ', '.join(':'.join(param) for param in node.params)
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: {node.id}({params}) : {node.type} {{<body>}}'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(IfThenElseNode)
    def visit(self, node, tabs=0):
        sons = [node.condition, node.if_body]
        text = ''
        if node.else_body:
            sons.append(node.else_body)
            text += 'else <body>'
        ans = '\t' * tabs + f'\\__IfThenElseNode: if <cond> then <body> {text} fi'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(WhileLoopNode)
    def visit(self, node, tabs=0):
        sons = [node.condition, node.body]
        ans = '\t' * tabs + f'\\__WhileLoopNode: while <cond> loop <body> pool'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(BlockNode)
    def visit(self, node, tabs=0):
        sons = node.expr
        ans = '\t' * tabs + f'\\__BlockNode: {{<expr> ... <expr>}}'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(LetInNode)
    def visit(self, node, tabs=0):
        sons = node.let_body + [node.in_body]
        ans = '\t' * tabs + f'\\__LetInNode: let {{<attr> ... <attr>}} in <expr>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(CaseOfNode)
    def visit(self, node, tabs=0):
        sons = [node.expr] + node.branches
        ans = '\t' * tabs + f'\\__CaseOfNode: case <expr> of {{<case> ... <case>}} esac'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(CaseExpresion)
    def visit(self, node, tabs=0):
        sons = [node.expr]
        ans = '\t' * tabs + f'\\__CaseExpresion: {node.id} : {node.type} => <expr>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in sons)
        return f'{ans}\n{body}'
    
    @visitor.when(AssignNode)
    def visit(self, node, tabs=0):
        sons = [node.expr]
        ans = '\t' * tabs + f'\\__AssignNode: {node.id} = <expr>'
        body = '\n'.join(self.visit(child, tabs + 1) for child in node.body)
        return f'{ans}\n{body}'
    
    @visitor.when(UnaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__{node.__class__.__name__} <expr>'
        right = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{right}'
   
    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__<expr> {node.__class__.__name__} <expr>'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ {node.__class__.__name__}: {node.lex}'
    
    @visitor.when(FunctionCallNode)
    def visit(self, node, tabs=0):
        obj = self.visit(node.obj, tabs + 1)
        ans = '\t' * tabs + f'\\__FunctionCallNode: <obj>.{node.id}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
        return f'{ans}\n{obj}\n{args}'
    
    @visitor.when(NewNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__NewNode: new {node.type}()'