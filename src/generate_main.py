import ast

class GenerateMain:
    name = 'class_generator'
    version = '0.0.1'

    def __init__(self):
        code = '''
class GeneratedClass:
    def __init__(self):
        pass
    def do_something(self):
        print("Doing something")
'''
        self.tree = ast.parse(code)

    def run(self):
        code = ast.unparse(self.tree)
        return code

if __name__ == '__main__':
    main_gen = GenerateMain()
    result_code = main_gen.run()
    with open('generated_main.py', 'w') as f:
        f.write(result_code)