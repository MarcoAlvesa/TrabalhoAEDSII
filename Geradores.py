import random
from autor import Autor
from livro import Livro
from editora import Editora
from faker import Faker

class Geradores:
    def __init__(self):
        self.fake = Faker()

    def calculate_special_digit(self, lst):
        digit = sum(v * ((i % 8) + 2) for i, v in enumerate(lst))
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    def generate_cnpj(self):                                                       
        cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for _ in range(8)]             
        for _ in range(2):                                                          
            cnpj.insert(0, self.calculate_special_digit(cnpj))
        return '{}{}.{}{}{}.{}{}{}-{}{}'.format(*cnpj)

    def gerar_autor(self, quantidade):
        autores = []
        for i in range(quantidade):
            id = i + 1
            nome = self.fake.name()
            datanasc = self.fake.date_of_birth(minimum_age=20, maximum_age=90)
            autores.append(Autor(id, nome, datanasc))
        return autores

    def gerar_editora(self, quantidade):
        editoras = []
        for i in range(quantidade):
            id = i + 1
            nome = self.fake.company()
            pais = self.fake.country()
            cnpj = self.generate_cnpj()
            editoras.append(Editora(id, nome, pais, cnpj))
        return editoras

    def gerar_livros(self, quantidade, autores, editoras):
        livros = []
        for i in range(quantidade):
            id = i + 1
            titulo = self.fake.sentence(nb_words=4)
            autor = random.choice(autores)
            editora = random.choice(editoras)
            anoPubli = random.randint(1900, 2024)
            livros.append(Livro(id, titulo, autor, editora, anoPubli))
        return livros
