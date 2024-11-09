import ast
from pathlib import Path
import os

class GenerateMain:
    name = 'class_generator'
    version = '0.0.1'

    def __init__(self):
        with open('main.txt', 'r') as f:
            code = f.read()
        self.tree = ast.parse(code)

    def run(self):
        code = ast.unparse(self.tree)
        return code

if __name__ == '__main__':
    path_to_dst = os.path.join(os.path.dirname(__file__), 'generated_main.py')
    main_gen = GenerateMain()
    result_code = main_gen.run()
    with open(path_to_dst, 'w') as f:
        f.write(result_code)