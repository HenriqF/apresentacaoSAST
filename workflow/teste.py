# workflow/teste.py
import os
import sqlite3

# CORREÇÃO 1: Lê a senha de variável de ambiente
SENHA_ADMIN = os.getenv("SENHA_ADMIN")

def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    # CORREÇÃO 2: Usa consulta parametrizada com '?' contra SQL Injection
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
    return cursor.fetchall()