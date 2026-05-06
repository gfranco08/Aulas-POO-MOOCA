import sqlite3

class Connect:
    def __init__(self):
        self.banco = sqlite3.connect('aula.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)")

    def inserir(self, u):
        self.cursor.execute("INSERT INTO user (nome, email) VALUES (?, ?)", (u.nome, u._email))
        self.banco.commit()

    def alterar(self, id, novo_nome):
        self.cursor.execute("UPDATE user SET nome = ? WHERE id = ?", (novo_nome, id))
        self.banco.commit()

    def listar(self):
        return self.cursor.execute("SELECT * FROM user").fetchall()




from connect import Connect
from usuario import Usuario

if __name__ == "__main__":
    db = Connect()
    
    lista = [
        Usuario("José", "marcos@email.com"),
        Usuario("Julia", "julia@email.com"),
        Usuario("Pedro", "pedro@email.com"),
        Usuario("Sofia", "sofia@email.com")
    ]

    for p in lista:
        db.inserir(p)
        
    db.alterar(1, "Marcos Editado")

    print(f"{'ID':<4} | {'NOME':<15} | {'EMAIL'}")
    print("-" * 40)
    for user in db.listar():
        print(f"{user[0]:<4} | {user[1]:<15} | {user[2]}")



        
class Usuario:
    def __init__(self, nome, email):
        self._nome = nome  
        self._email = email

    @property 
    def nome(self):
        return self._nome

    @nome.setter 
    def nome(self, valor):
        self._nome = valor


