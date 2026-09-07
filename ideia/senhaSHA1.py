import hashlib

senha = input()
senha_bytes = senha.encode("utf-8")
senha_hash = hashlib.sha1(senha_bytes).hexdigest()

print(senha_hash)



