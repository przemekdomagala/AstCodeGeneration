import ast
import os
import pickle

def code_to_ast(src_file):
    with open(src_file, 'r') as f:
        code = f.read()

    tree = ast.parse(code)

    pickle_file = os.path.join(os.path.dirname(__file__), 'main.pkl')

    tree = test_append(tree)

    with open(pickle_file, 'wb') as f:
        pickle.dump(tree, f)

def ast_to_code(dst_file):
    pickle_file = os.path.join(os.path.dirname(__file__), 'main.pkl')
    
    with open(pickle_file, 'rb') as f:
        tree = pickle.load(f)

    code = ast.unparse(tree)

    with open(dst_file, 'w') as f:
        f.write(code)

def test_append(tree):
    function_def = tree.body[0].body[1]
    new_arg = ast.arg(arg='test_arg', annotation=None)
    function_def.args.args.append(new_arg)
    default_value = ast.Constant(value=1)
    function_def.args.defaults.append(default_value)
    return tree

if __name__ == '__main__':
    dst_file = os.path.join(os.path.dirname(__file__), 'main.py')
    src_file = os.path.join(os.path.dirname(__file__), '..', 'generated_main.py')
    code_to_ast(src_file)
    ast_to_code(dst_file)
