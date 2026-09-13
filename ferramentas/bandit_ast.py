import ast

python_code = """

def codigo_legal(argumento):
    
    if argumento == "ruim":
        return "FALSO!"

    return f"SAST {argumento}"

result = codigo_legal("BANDIT")

"""

arvore = ast.parse(python_code)
print(ast.dump(arvore, indent=2))