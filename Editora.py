class Editora:
    def __init__(self, id, nome, pais, cnpj):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.cnpj = cnpj
    def toString(self):
        return f"Editora: [{self.id}] Nome: {self.nome}, Pais: {self.pais}, CNPJ: {self.cnpj}"
