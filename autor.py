class Autor:
    def __init__(self, id, nome, datanasc):
        self.id = id
        self.nome = nome
        self.datanasc = datanasc

    def __str__(self):
        return f"Autor: [{self.id}] Nome: {self.nome}, Data de nascimento: {self.datanasc}"
