import random
from autor import Autor
from livro import Livro
from editora import Editora
from faker import Faker

class Geradores:
    def __init__(self):
        self.cnpj = self.generate_cnpj()

    def calculate_special_digit(self, lst):
        digit = sum(v * ((i % 8) + 2) for i, v in enumerate(lst))
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    def generate_cnpj(self):                                                       
        cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for _ in range(8)]             
        for _ in range(2):                                                          
            cnpj.insert(0, self.calculate_special_digit(cnpj))
        return '{}{}.{}{}{}.{}{}{}-{}{}'.format(*cnpj)

    def get_cnpj(self):
        return self.cnpj
    
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
            cnpj = generate_cnpj()
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
