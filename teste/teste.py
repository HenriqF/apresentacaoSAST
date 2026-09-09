# teste.py
import sqlite3

# FALHA 1: Senha/chave de acesso gravada direto no arquivo
TOKEN_SECRETO = "AWS_SECRET_123456" 

def buscar_usuario(nome):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    
    # FALHA 2: SQL Injection (junta texto direto na consulta)
    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"
    cursor.execute(query)
    return cursor.fetchall()