import ast

python_code = ""
with open("github.py", "r") as f:
    python_code = f.read()
parsed_ast = ast.parse(python_code)

assignments = [no for no in ast.walk(parsed_ast) if isinstance(no, ast.Assign)]
for assignment in assignments:
    target = assignment.targets[0]
    if not isinstance(target, ast.Name):
        continue
    if "GITHUB" in target.id:
        print(F"VULNERABILIDADE NA LINHA {assignment.lineno}: {target.id}") 








