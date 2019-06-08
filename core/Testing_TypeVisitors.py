# Build AST

# In[46]:


from cmp.visitors import *
from cmp.evaluation import *


def build_AST(G, text):
    print('=================== TEXT ======================')
    print(text)
    print('================== TOKENS =====================')
    tokens = tokenize_text(text)
    pprint_tokens(tokens)
    print('=================== PARSE =====================')
    parser = LR1Parser(G)
    print(parser([t.token_type for t in tokens], get_shift_reduce=True))
    parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
    print('\n'.join(repr(x) for x in parse))
    print('==================== AST ======================')
    ast = evaluate_reverse_parse(parse, operations, tokens)
    formatter = FormatVisitor()
    tree = formatter.visit(ast)
    print(tree)
    return ast

ast = build_AST(CoolGrammar, text)


# ## Chequeo Semantico
# 
# En `cmp.semantic` se distribuyen una serie de clases que funcionarán como soporte para la fase de chequeo semántico.

# In[47]:


from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import ErrorType
from cmp.semantic import Context


# - La clase `SemanticError` hereda de `Exception` para funcionar como mecanismo para manejar errores en los contextos. El campo `text` que poseen las instancias de `SemanticError` permite obtener el texto de error con el que se construyó.
# - Las clases `Attribute` y `Method` funcionan como contenedores de los datos necesarios para representar los atributos y métodos del lenguaje respectivamente. Del primero se almacena el nombre del campo (un `str)` y su tipo (una instancia de `Type`). Del segundo se almacenan: nombre del método (`str`), nombre de los parámetros (`list<str>`), tipos de los parámetros (`list<Type>`) y el tipo de retorno (`Type`).
# - La clase `Type` funciona como descriptor de todos los atributos y métodos con que cuentan los tipos del lenguaje. Esta clase permite crear instancias a partir del nombre del tipo (`Type(name)`) y posteriormente actualizar su definición con:
#     - tipo padre: `set_parent(...)`.
#     - atributos: `get_attributes(...)` y `define_attribute(...)`.
#     - métodos: `get_method(...)` y `define_method(...)`.
# 
# > Para más información se recomienda revisar el código fuente disponible en `cmp.semantic`.
# 
# - La clase `ErrorType` puede usarse para manejar las situaciones en las que se refiere un tipo que no ha sido declarado. Esto nos permitirá detectar más errores que detener el chequeo semántico al primer error. Las instancias de `ErrorType` tiene la particularidad de ser iguales entre sí y a cualquier instancia de `Type`. Además, el tipo `ErrorType` se conforma (en el sentido de herencia) a todo tipo y viceversa.
# - La clase `Context` permite controlar los tipos que han sido definidos en el lenguaje.
#     - definir un tipo: `create_type(...)`.
#     - obtener un tipo: `get_type(...)`.

# ### Type Collector

# In[48]:


class TypeCollector(object):
    def __init__(self, errors=[]):
        self.context = None
        self.errors = errors
        self.type_level = {}
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        self.context = Context()
        # Your code here!!!
        self.context.create_type('int') # ask for missing built-in types
        self.context.create_type('string')
        self.context.create_type('bool')
        self.context.create_type('IO')
        self.context.create_type('SELF_TYPE')
        self.context.create_type('AUTO_TYPE')
        
        for def_class in node.declarations:
            self.visit(def_class)
             
        # comparison for sort node.declarations
        def get_type_level(typex):
            try:
                parent = self.type_level[typex]
            except KeyError:
                return 0
            
            if parent == 0:
                self.errors.append('Cyclic heritage.')
            elif type(parent) is not int:
                self.type_level[typex] = 0 if parent else 1
                if type(parent) is str:
                    self.type_level[typex] = get_type_level(parent) + 1
                
            return self.type_level[typex]
        
        node.declarations.sort(key = lambda node: get_type_level(node.id))
                
                
        
    # Your code here!!!
    # ????
    @visitor.when(ClassDeclarationNode)
    def visit(self, node):
        try:
            self.context.create_type(node.id)
            self.type_level[node.id] = node.parent
        except SemanticError as ex:
            self.errors.append(ex.text)


#     

# In[49]:


errors = []

collector = TypeCollector(errors)
collector.visit(ast)

context = collector.context

print('Errors:', errors)
print('Context:')
print(context)

assert errors == []


# ### Type Builder

# In[50]:


class TypeBuilder:
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.errors = errors
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    # Your code here!!!
    # ????
    @visitor.when(ProgramNode)
    def visit(self, node):
        for def_class in node.declarations:
            self.visit(def_class)
            
        try:
            self.context.get_type('Main').get_method('main')
        except SemanticError:
            self.errors.append('The class "Main" and his method "main" are needed.')
            
    
    @visitor.when(ClassDeclarationNode)
    def visit(self, node):
        self.current_type = self.context.get_type(node.id)
        
        if node.parent:
            try:
                parent_type = self.context.get_type(node.parent)
                self.current_type.set_parent(parent_type)
            except SemanticError as ex:
                self.errors.append(ex.text)
        
        for feature in node.features:
            self.visit(feature)
            
    @visitor.when(AttrDeclarationNode)
    def visit(self, node):
        try:
            attr_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            attr_type = ErrorType()
            
        try:
            self.current_type.define_attribute(node.id, attr_type)
        except SemanticError as ex:
            self.errors.append(ex.text)
        
    @visitor.when(FuncDeclarationNode)
    def visit(self, node):
        arg_names, arg_types = [], []
        for idx, typex in node.params:
            try:
                arg_type = self.context.get_type(typex)
            except SemanticError as ex:
                self.errors.append(ex.text)
                arg_type = ErrorType()
                
            arg_names.append(idx)
            arg_types.append(arg_type)
        
        try:
            ret_type = VoidType() if node.type == 'void' else self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            ret_type = ErrorType()
        
        try:
            self.current_type.define_method(node.id, arg_names, arg_types, ret_type)
        except SemanticError as ex:
            self.errors.append(ex.text)


#    

# In[51]:


builder = TypeBuilder(context, errors)
builder.visit(ast)

print('Errors:', errors)
print('Context:')
print(context)


# ### Chequeo de Tipos
# 
# Estaremos validando que el programa haga un uso correcto de los tipos definidos. Recordemos algunas de las características del lenguaje que queremos comprobar:
# - Todos los métodos son de instancia y dentro de ellos es visible `self` _(solo lectura)_, cuyo tipo estático coincide con el de la clase que implementa el método.
# - Al invocar un método, se evalúa primero la expresión que devuelve el objeto, luego los parámetros, y por último se llama la función.
# - Todos los atributos son privados y todos los métodos son públicos.
# - Un método se puede sobrescribir sí y solo sí se mantiene exactamente la misma definición para los tipos de retorno y de los argumentos.
# - Las operaciones `+`, `-`, `*` y `/` están definidas únicamente entre valores enteros, y devuelven enteros.

# In[52]:


from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import ErrorType, IntType


# In[53]:


WRONG_SIGNATURE = 'Method "%s" already defined in "%s" with a different signature.'
SELF_IS_READONLY = 'Variable "self" is read-only.'
LOCAL_ALREADY_DEFINED = 'Variable "%s" is already defined in method "%s".'
INCOMPATIBLE_TYPES = 'Cannot convert "%s" into "%s".'
VARIABLE_NOT_DEFINED = 'Variable "%s" is not defined in "%s".'
INVALID_OPERATION = 'Operation is not defined between "%s" and "%s".'


# ### Scope
# 
# Se provee una implementación de la clase `Scope` en `cmp.semantic`. Esta clase nos permitirá gestionar las variables definidas en los distintos niveles de visibilidad, así como saber con qué tipo se definieron. Los métodos fundamentales son:
# - `create_child`: Crea un `scope` hijo que hereda las variables visibles hasta ese momento en el `scope` padre.
# - `define_variable`: Registra localmente una variable en el `scope` a partir de su nombre y tipo.
# - `find_variable`: Devuelve un `VariableInfo` con la información de la variable consultada (a partir de su nombre). La variable devuelta no tiene por qué estar definida localmente. En caso de que la variable no esté definida devuelve `None`.
# - `is_defined`: Indica si la variable consultada es visible en el `scope`.
# - `is_local`: Indica si la variable consultada está definida localmente en el `scope`.

# In[54]:


from cmp.semantic import Scope


# ### Type Checker

# In[55]:


class TypeChecker:
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.current_method = None
        self.errors = errors

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope()
        for declaration in node.declarations:
            self.visit(declaration, scope.create_child())
        return scope

    @visitor.when(ClassDeclarationNode)
    def visit(self, node, scope):
        self.current_type = self.context.get_type(node.id)
        
        scope.define_variable('self', self.current_type)
        for attr in self.current_type.attributes:
            scope.define_variable(attr.name, attr.type)
            
        for feature in node.features:
            self.visit(feature, scope.create_child())
        
    @visitor.when(AttrDeclarationNode)
    def visit(self, node, scope):
        pass

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        self.current_method = self.current_type.get_method(node.id)
        
        for pname, ptype in zip(self.current_method.param_names, self.current_method.param_types):
            scope.define_variable(pname, ptype)
            
        for expr in node.body:
            self.visit(expr, scope)
            
        last_expr = node.body[-1]
        last_expr_type = last_expr.computed_type
        method_rtn_type = self.current_method.return_type
        
        if not last_expr_type.conforms_to(method_rtn_type):
            self.errors.append(INCOMPATIBLE_TYPES.replace('%s', last_expr_type.name, 1).replace('%s', method_rtn_type.name, 1))

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope)
        expr_type = node.expr.computed_type
        
        try:
            node_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            node_type = ErrorType()
        
        if not expr_type.conforms_to(node_type):
            self.errors.append(INCOMPATIBLE_TYPES.replace('%s', expr_type.name, 1).replace('%s', node_type.name, 1))
          
        if not scope.is_defined(node.id):
            scope.define_variable(node.id, node_type)
        else:
            self.errors.append(LOCAL_ALREADY_DEFINED.replace('%s', node.id, 1).replace('%s', self.current_method.name, 1))
        
        node.computed_type = node_type
            
    @visitor.when(AssignNode)
    def visit(self, node, scope):
        self.visit(node.expr, scope)
        expr_type = node.expr.computed_type
        
        if scope.is_defined(node.id):
            var = scope.find_variable(node.id)
            node_type = var.type       
            
            if var.name == 'self':
                self.errors.append(SELF_IS_READONLY)
            elif not expr_type.conforms_to(node_type):
                self.errors.append(INCOMPATIBLE_TYPES.replace('%s', expr_type.name, 1).replace('%s', node_type.name, 1))
        else:
            self.errors.append(VARIABLE_NOT_DEFINED.replace('%s', node.id, 1).replace('%s', self.current_method.name, 1))
            node_type = ErrorType()
        
        node.computed_type = node_type
    
    @visitor.when(FunctionCallNode)
    def visit(self, node, scope):
        self.visit(node.obj, scope)
        obj_type = node.obj.computed_type
        
        try:
            obj_method = obj_type.get_method(node.id)
            
            if len(node.args) == len(obj_method.param_types):
                for arg, param_type in zip(node.args, obj_method.param_types):
                    self.visit(arg, scope)
                    arg_type = arg.computed_type
                    
                    if not arg_type.conforms_to(param_type):
                        self.errors.append(INCOMPATIBLE_TYPES.replace('%s', arg_type.name, 1).replace('%s', param_type.name, 1))
            else:
                self.errors.append(f'Method "{obj_method.name}" of "{obj_type.name}" only accepts {len(obj_method.param_types)} argument(s)')
            
            node_type = obj_method.return_type
        except SemanticError as ex:
            self.errors.append(ex.text)
            node_type = ErrorType()
            
        node.computed_type = node_type
    
    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        self.visit(node.left, scope)
        left_type = node.left.computed_type
        
        self.visit(node.right, scope)
        right_type = node.right.computed_type
        
        if not left_type.conforms_to(IntType()) or not right_type.conforms_to(IntType()):
            self.errors.append(INVALID_OPERATION.replace('%s', left_type.name, 1).replace('%s', right_type.name, 1))
            node_type = ErrorType()
        else:
            node_type = IntType()
            
        node.computed_type = node_type
    
    @visitor.when(IntegerNode)
    def visit(self, node, scope):
        node.computed_type = IntType()

    @visitor.when(IdNode)
    def visit(self, node, scope):
        if scope.is_defined(node.lex):
            var = scope.find_variable(node.lex)
            node_type = var.type       
        else:
            self.errors.append(VARIABLE_NOT_DEFINED.replace('%s', node.lex, 1).replace('%s', self.current_method.name, 1))
            node_type = ErrorType()
        
        node.computed_type = node_type

    @visitor.when(NewNode)
    def visit(self, node, scope):
        try:
            node_type = self.context.get_type(node.type)
        except SemanticError as ex:
            self.errors.append(ex.text)
            node_type = ErrorType()
            
        node.computed_type = node_type


# ## Pipeline

# In[56]:


def run_pipeline(G, text):
    ast = build_AST(G, text)
    print('============== COLLECTING TYPES ===============')
    errors = []
    collector = TypeCollector(errors)
    collector.visit(ast)
    context = collector.context
    print('Errors:', errors)
    print('Context:')
    print(context)
    print('=============== BUILDING TYPES ================')
    builder = TypeBuilder(context, errors)
    builder.visit(ast)
    print('Errors: [')
    for error in errors:
        print('\t', error)
    print(']')
    print('Context:')
    print(context)
    print('=============== CHECKING TYPES ================')
    checker = TypeChecker(context, errors)
    scope = checker.visit(ast)
    print('Errors: [')
    for error in errors:
        print('\t', error)
    print(']')
    return ast, errors, context, scope


# In[57]:


ast, errors, context, scope = run_pipeline(CoolGrammar, text)

