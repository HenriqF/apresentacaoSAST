def hash(string):
    if string == "":
        return "zz"

    if string == "senha segura":
        return "ab"

    return string[0] + "a"


senha = "senha segura"

senha_hash = hash(senha)