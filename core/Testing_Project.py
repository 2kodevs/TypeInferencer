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
    #print(parser([t.token_type for t in tokens], get_shift_reduce=True))
    parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
    #print('\n'.join(repr(x) for x in parse))
    print('==================== AST ======================')
    ast = evaluate_reverse_parse(parse, operations, tokens)
    formatter = FormatVisitor()
    tree = formatter.visit(ast)
    print(tree)
    return ast


text = '''
class A inherits SELF_TYPE { } ;
class Main {
    a : Bool ;
    b : Int <- 666 ;
    main ( console : IO ) : Bool {
        a <- true ;
        {
            let c : Int <- 0 in c + b ;
        } ;
        if b then { b <- 0 ; } else b <- 1 fi ;
        while a loop b <- b + 1 pool ;
        a ;
    } ;
} ;
'''

text2 = '''
class Main {
    main ( console : IO ) : C {
        if true then new C else new B fi ;
    } ;
} ;

class A { } ;

class B inherits A { } ;

class C inherits A { } ;

'''

text3 = '''
class Main {
    main ( console : IO ) : C {
        if true then "tno" else new B fi ;
    } ;
} ;

class A { } ;

class B { } ;

class C { } ;

'''

text4 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : AUTO_TYPE <- 666 ;
    main ( console : IO ) : Bool {
        case b of {
            r1 : Bool => new A ;
            r2 : SELF_TYPE => new Main ;
            }
        esac ;
        a ;
    } ;
} ;

class A { } ;
'''

text5 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : Int ;
    d : AUTO_TYPE ;
    main ( console : IO ) : AUTO_TYPE {
        case b of {
            r1 : Bool => new A ;
            r2 : SELF_TYPE => new Main ;
            }
        esac ;
        d ;
    } ;


} ;

class A { } ;
'''

text6 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : AUTO_TYPE <- self . wait ( tRuE ) ;
    d : AUTO_TYPE ;
    main ( console : IO ) : AUTO_TYPE {
        case b of {
            r1 : Bool => new A ;
            r2 : SELF_TYPE => new Main ;
            }
        esac ;
        d <- self . wait ( 5 ) ;
        d ;
    } ;

    wait ( x : AUTO_TYPE ) : AUTO_TYPE {
        x ;
    } ;


} ;

class A { } ;
'''

text7 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : Int ;
    d : AUTO_TYPE ;
    main ( console : IO ) : AUTO_TYPE {
        if d then d fi ;
    } ;
} ;
'''

text8 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : AUTO_TYPE ;
    d : AUTO_TYPE ;
    main ( console : IO ) : Int {
        if d then c else d fi ;
    } ;
} ;

class A { 
    repet ( param : IO ) : String {
        "output" ;
    } ;
} ;

class B { } ;

class C inherits A { 
    repet ( param : Int ) : String {
        "output" ;
    } ;
} ;
'''

text9 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : AUTO_TYPE ;
    d : AUTO_TYPE ;
    main ( console : IO ) : Int {
        
        let k : AUTO_TYPE in k ;
    } ;
} ;
'''

text10 = '''
class Main {
    
    main ( console : IO ) : AUTO_TYPE {
        5 ;
    } ;

    is_null ( x : Int ) : AUTO_TYPE {
        isvoid ( x ) ;
    } ;

} ;

'''

text11 = '''
class Main {
    a : Bool ;
    b : Int <- true ;
    c : AUTO_TYPE <- self . wait ( tRuE ) ;
    d : AUTO_TYPE ;
    main ( console : IO ) : AUTO_TYPE {
        case b of {
            r1 : Bool => new A ;
            r2 : SELF_TYPE => new Main ;
            }
        esac ;
        d <- wait ( 5 ) ;
        d ;
    } ;

    wait ( x : AUTO_TYPE ) : AUTO_TYPE {
        x ;
    } ;

} ;

'''

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
    print('=============== CHECKING TYPES ================')
    checker = TypeChecker(context, [])
    scope = checker.visit(ast)
    print('=============== INFERING TYPES ================')
    inferer = InferenceVisitor(context, [])
    while True:
        old = scope.count_auto()
        scope = inferer.visit(ast)
        if old == scope.count_auto():
            break
    inferer = InferenceVisitor(context, errors)
    scope = inferer.visit(ast)
    print('Errors: [')
    for error in errors:
        print('\t', error)
    print(']')
    print('Context:')
    print(context)
    formatter = ComputedVisitor()
    tree = formatter.visit(ast)
    print(tree)
    return ast, errors, context, scope


ast, errors, context, scope = run_pipeline(CoolGrammar, text11)
print('NUM of AUTO_TYPES:  ', scope.count_auto())

