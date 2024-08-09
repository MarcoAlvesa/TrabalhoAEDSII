import GeradorDocumentos

class Editora:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = GeradorDocumentos.GeradorCNPJ().get_cnpj()  # Gera o CNPJ

    def getcnpj(self):
        return self.cnpj
