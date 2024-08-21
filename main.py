from autor import Autor
from editora import Editora
from livro import Livro
import  time
editora = Editora()
autor = Autor()
livro = Livro()

autor.gerador(10)
editora.gerador(5)
livro.gerador(100)
livro.printBase()
autor.bubble_sort_base()
editora.bubble_sort_base()


while True:
    print(f'\n[0]-> Sair'
          f'\n[1]-> Autores'
          f'\n[2]-> Editoras'
          f'\n[3]-> Livros')
    escolha = int(input(f'Escolha em qual base deseja pesquisar: '))
    if escolha == 0:
        break
    elif escolha == 1:
        pesquisa = int(input('Escolha o ID a ser pesquisado: '))
        autor.pesquisa_sequencial(pesquisa)
        autor.pesquisa_binaria(pesquisa)
    elif escolha == 2:
        pesquisa = int(input('Escolha o ID a ser pesquisado: '))
        editora.pesquisa_sequencial(pesquisa)
        editora.pesquisa_binaria(pesquisa)
#     elif escolha == 3:
#         pesquisa = int(input('Escolha o ID a ser pesquisado: '))
#         livro.pesquisa_sequencial(pesquisa)
#         livro.pesquisa_binaria(pesquisa)
