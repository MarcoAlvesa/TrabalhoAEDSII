from geradores import Geradores
import random

geradores = Geradores()

autores = geradores.gerar_autor(50)
editoras = geradores.gerar_editora(50)
livros = geradores.gerar_livros(50, autores, editoras)

random.shuffle(autores)
random.shuffle(editoras)
random.shuffle(livros)

for editora in editoras:
    print(f"ID: {editora.id}, nome: {editora.nome}, pais: {editora.pais}, cnpj: {editora.cnpj}")

for autor in autores:
    print(f"ID: {autor.id}, nome: {autor.nome}, data de nascimento: {autor.datanasc}")

for livro in livros:
    print(f"ID: {livro.id}, Titulo: {livro.titulo}, Autor: {livro.autor.nome}, Editora: {livro.editora.nome}, Ano publicado: {livro.anoPubli}")

