# workflow/teste.py
import sqlite3

# FALHA 1: Senha em texto puro (Hardcoded password)
SENHA_ADMIN = "123456"

def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    # FALHA 2: SQL Injection (O Bandit vai pegar essa linha)
    cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{nome}'")
    return cursor.fetchall()