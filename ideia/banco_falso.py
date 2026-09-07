NOME_BANCO = "NOME"
SENHA_BANCO = "9658YUO213HINJDSAFLGDSAF9"

def buscar_aluno(matricula):
    conexao = banco.conectar(NOME_BANCO, SENHA_BANCO)
    busca = f"SELECT * FROM aluno WHERE matricula = {matricula}"
    conexao.executar(busca)






class banco:
    def conectar(nome, senha):
        return conexao


class conexao:
    def executar(query):
        return