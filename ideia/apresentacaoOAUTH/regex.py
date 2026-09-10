import re

with open("github.py", "r") as file:
    conteudo = file.read()

    for vul in re.finditer(r"""(['"])([\w]{20}|[\w]{40})\1""", conteudo):
    
        print(f"Vulnerabilidade em: {vul.start()} - {vul.end()}")
        print(conteudo[vul.start():vul.end()])
