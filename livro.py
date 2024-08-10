class Livro:
    def __init__(self, id, titulo, autor, editora, anoPubli):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.anoPubli = anoPubli

    def toString(self):
        return f"Livro: [{self.id}] Titulo: {self.titulo}, Autor: {self.autor.nome}, Editora: {self.editora.nome}, Ano: {self.anoPubli} "
