from autor import Autor
from editora import Editora
from livro import Livro

editora = Editora()
autor = Autor()
livro = Livro()
tam_autores = int(input("Insira o tamanho da base [Autores]: "))
tam_editoras = int(input("Insira o tamanho da base [Editoras]: "))
tam_livros = int(input("Insira o tamanho da base [Livros]: "))
print(f'Gerando base: [Autores] aguarde!')
print(50*'=')
autor.gerador(tam_autores)
print(f'\nGerando base: [Editoras] aguarde!')
print(50*'=')
editora.gerador(tam_editoras)
print(f'\nGerando base: [Livros] aguarde!')
print(50*'=')
livro.gerador(tam_livros)





resposta = str(input('Deseja imprimir a base de autores? [S/N]: ').upper())
if resposta == 'S':
    autor.printBase()

resposta = str(input('Deseja imprimir a base de editoras? [S/N]: ').upper())
if resposta == 'S':
    editora.printBase()

resposta = str(input('Deseja imprimir a base de livros? [S/N]: ')).upper()
if resposta == 'S':
    livro.printBase()

print(f'{50*"="}\n{15*" "}Ordenando as bases\n{"="*50}')
print(f'Ordenando base [Autores] aguarde!')
autor.bubble_sort_base()
resposta = str(input('Deseja imprimir a base [autores] ordenada? [S/N]: ').upper())
if resposta == 'S':
    autor.printBase()


print(f'{50*"="}')
print(f'Ordenando base [Editoras] aguarde!')
editora.bubble_sort_base()
resposta = str(input('Deseja imprimir a base [editoras] ordenada? [S/N]: ').upper())
if resposta == 'S':
    editora.printBase()
print(f'{50*"="}')
print(f'Ordenando base [Livros] aguarde!')
livro.bubble_sort_base()
resposta = str(input('Deseja imprimir a base [livros]? [S/N]: ')).upper()
if resposta == 'S':
    livro.printBase()

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
    elif escolha == 3:
        pesquisa = int(input('Escolha o ID a ser pesquisado: '))
        livro.pesquisa_sequencial(pesquisa)
        livro.pesquisa_binaria(pesquisa)
    else:
        print(f'{10*"="}>Insira uma opção válida!<{10*"="}')
