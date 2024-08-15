import random
from autor import Autor
from livro import Livro
from editora import Editora
from faker import Faker
import pickle

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

    def gerar_autor(self, quantidade, arquivo_txt='autores_random.txt', arquivo_bin='autores_random.bin'):
        autores = []
        for i in range(quantidade):
            id = i + 1
            nome = self.fake.name()
            datanasc = self.fake.date_of_birth(minimum_age=20, maximum_age=90)
            autores.append(f"ID: {id}, Nome: {nome}, Data de Nascimento: {datanasc}")

        random.shuffle(autores)

        with open(self.arquivo_txt, 'w') as arquivo_txt:
            for autor in autores:
                arquivo_txt.write(autor + '\n')
        with open(self.arquivo_bin, 'wd') as arquivo_bin:
            pickle.dump(autores, arquivo_bin)

        print(f"Arquivo de texto'{self.arquivo_txt}' e arquivo binário '{self.arquivo_bin}' criado com sucesso.")
        return autores

    def gerar_editora(self, quantidade, arquivo_txt='editora_random.txt', arquivo_bin='editora_random.bin'):
        editoras = []
        for i in range(quantidade):
            id = i + 1
            nome = self.fake.company()
            pais = self.fake.country()
            cnpj = self.generate_cnpj()
            editoras.append(f"ID: {id}, Nome: {nome}, Pais: {pais}, CNPJ: {cnpj}")
        random.shuffle(editoras)
        
        with open(self.arquivo_txt, 'w') as arquivo_txt:
            for editora in editoras:
                arquivo_txt.write(editora + '\n')
        with open(self.arquivo_bin, 'wd') as arquivo_bin:
            pickle.dump(editoras, arquivo_bin)

        print(f"Arquivo de texto'{self.arquivo_txt}' e arquivo binário '{self.arquivo_bin}' criado com sucesso.")
        return editoras

    def gerar_livros(self, quantidade, autores, editoras, arquivo_txt= 'livros_random.txt', arquivo_bin = 'livros_random.bin'):
        livros = []
        for i in range(quantidade):
            id = i + 1
            titulo = self.fake.sentence(nb_words=4)
            autor = random.choice(autores)
            editora = random.choice(editoras)
            anoPubli = random.randint(1900, 2024)
            livros.append(f"ID: {id}, Titulo: {titulo}, Autor: {autor.nome}, Editora: {editora.nome}, Ano de Publicação: {anoPubli}")
        random.shuffle(livros)
        with open(self.arquivo_txt, 'w') as arquivo_txt:
            for livro in livros:
                arquivo_txt.write(livro + '\n')

        with open(self.arquivo_bin, 'wd') as arquivo_bin:
            pickle.dump(livros, arquivo_bin)
        
        print(f"Arquivo de texto'{self.arquivo_txt}' e arquivo binário '{self.arquivo_bin}' criado com sucesso.")
        return livros
