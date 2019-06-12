import eel
import logging
from cmp.visitors import *
from cmp.evaluation import *


def build_AST(G, text):
    data, err = [], False
    ast = None
    txt = '================== TOKENS =====================\n'
    tokens = tokenize_text(text)
    txt += format_tokens(tokens)
    data.append(txt)
    txt = '=================== PARSE =====================\n'
    parser = LR1Parser(G)
    #print(parser([t.token_type for t in tokens], get_shift_reduce=True))
    try:
        parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
    except:
        err = True
        txt = 'Impossible to parse\n'
    #print('\n'.join(repr(x) for x in parse))
    if not err:
        data.append(txt)
        txt = '==================== AST ======================\n'
        ast = evaluate_reverse_parse(parse, operations, tokens)
        formatter = FormatVisitor()
        tree = formatter.visit(ast)
        txt += str(tree)
    return ast, '\n\n'.join(data)

def error_formatter(errors):
    txt = 'Errors: [\n'
    for error in errors:
        text += f'\t{error}\n'
    txt += ']\n'

def run_pipeline(G, text):
    data, err = [], False
    ast, txt = build_AST(G, text)
    errors = context = scope = None
    data.append(txt)
    if ast:
        txt = '============== COLLECTING TYPES ===============\n'
        errors = []
        collector = TypeCollector(errors)
        collector.visit(ast)
        context = collector.context
        if len(errors)
            txt += error_formatter(errors)
            err = True
        txt += '\nContext:\n'
        txt += str(context)
        data.append(txt)
        errors.clear()
        txt = '=============== BUILDING TYPES ================\n'
        builder = TypeBuilder(context, errors)
        builder.visit(ast)
        if len(errors)
            txt += error_formatter(errors)
            err = True
        errors.clear()
        data.append(txt)
        txt = '=============== CHECKING TYPES ================\n'
        checker = TypeChecker(context, errors)
        scope = checker.visit(ast)
        if len(errors)
            txt += error_formatter(errors)
            err = True
        errors.clear()
        data.append(txt)
        txt = '=============== INFERING TYPES ================\n'
        inferer = InferenceVisitor(context, errors)
        while True:
            old = scope.count_auto()
            scope = inferer.visit(ast)
            if old == scope.count_auto():
                break
        errors.clear()
        scope = inferer.visit(ast)
        if len(errors)
            txt += error_formatter(errors)
            err = True
        errors.clear()
        txt += '\nContext:\n'
        txt += str(context)
        formatter = ComputedVisitor()
        tree = formatter.visit(ast)
        txt += str(tree)
    return '\n\n'.join(data)

@eel.expose
def compile(text):
    return run_pipeline(CoolGrammar, text)

def main():
    eel.init('web')

    eel_options = {'port': 8045}
    eel.start('index.html', size=(1000, 860), options=eel_options, block=False)

    while True:
        eel.sleep(0.1)


if __name__ == '__main__':
    main()