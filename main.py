import random
from autor import Autor
from livro import Livro
from editora import Editora
from faker import Faker

def gerar_autor(quantidade):
    Autor = []
    for i in range(quantidade):
        id = i + 1
        nome = fake.name()
        datanasc = fake.date_of_birth(minimum_age=20, maximum_age=90)
        Autor.append(Autor(id, nome, datanasc))
    return Autor

def gerar_editora(quantidade):
    editora = []
    for i in range(quantidade):
        id = i + 1
        nome = fake.company()
        pais = fake.country()
        cnpj =
        editora.append(Editora(id, nome, pais, cnpj))
    return editora

def gerar_livros(quantidade, Autor, editora):
    livros = []
    for i in range(quantidade):
        id = i + 1
        titulo = fake.sentence(nb_word=4)
        autor = random.choice(Autor)
        editora = random.choice(editora)
        anoPubli = random.randint(1900, 2024)
        livros.append(Livro(id, titulo, autor, editora, anoPubli))
    return livros