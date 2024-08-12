import math

from geradores import Geradores
from merge import Merge
from escreveArquivotxt import EscreveArquivotxt
from escreverArquivobin import EscreverArquivobin
from pesquisas import Pesquisas
import time

# Instanciando o gerador e a quantidade de entidades
geradores = Geradores()
tamGeradores = 10
# Escrita das pesquisas
escrevePesquisatxt = EscreveArquivotxt(f"pesquisa na base.txt")
escrevePesquisabin = EscreverArquivobin(f"pesquisa na base.dat")


for c in range(0, 3):
    tamGeradores = int(input('Tamanho da base: '))

    # Instanciando escrita das bases txt e dat
    escreveArquivotxt = EscreveArquivotxt(f'BASE_{c + 1}.txt')
    escreveArquivobin = EscreverArquivobin(f'BASE_{c + 1}.dat')

    # ====================================GERANDO BASE DESORDENADA====================================
    print(f'Gerando a base de dados com tamanho: [{tamGeradores}]')
    autores = geradores.gerar_autor(tamGeradores)
    editoras = geradores.gerar_editora(tamGeradores)
    livros = geradores.gerar_livros(tamGeradores, autores, editoras)

    # Escrevendo as bases de dados DESORDENADA no arquivo txt
    escreveArquivotxt.escreveTexto(f'{20*"="}Base DESORDENADA{20*"="}\n')
    escreveArquivotxt.escreveLista(livros)
    escreveArquivotxt.escreveLista(autores)
    escreveArquivotxt.escreveLista(editoras)

    # Escrevendo as bases de dados DESORDENADA no arquivo binario
    escreveArquivobin.escreveTexto(f'{20*"="}Base DESORDENADA{20*"="}\n')
    escreveArquivobin.escreveLista(livros)
    escreveArquivobin.escreveLista(autores)
    escreveArquivobin.escreveLista(editoras)

    # ====================================ORDENANDO BASE====================================
    # Ordenando as bases de dados por meio da Merge Sort
    tInicioAutormerge = time.time()
    merge_autores = Merge(autores, key=lambda autor: autor.id)
    merge_autores.sort()
    tFimAtutormerge = time.time()
    tInicioEditoramerge = time.time()
    merge_editora = Merge(editoras, key=lambda editora: editora.id)
    merge_editora.sort()
    tFimEditoramerge = time.time()
    tInicioLivromerge = time.time()
    merge_livros = Merge(livros, key=lambda livro: livro.id)
    merge_livros.sort()
    tFimlivromerge = time.time()
    tempoAutormerge = tFimAtutormerge-tInicioAutormerge
    tempoEditoramerge = tFimEditoramerge-tInicioEditoramerge
    tempoLivromerge = tFimlivromerge-tInicioLivromerge

    # Escrevendo a base de dados ORDENADA no arquivo txt
    escreveArquivotxt.escreveTexto(f'{20*"="}Base ORDENADA{20*"="}\n')
    escreveArquivotxt.escreveLista(livros)
    escreveArquivotxt.escreveLista(autores)
    escreveArquivotxt.escreveLista(editoras)
    escreveArquivotxt.escreveTexto(f'Tempo de ordenação base Autores: {tempoAutormerge:.6f}')
    escreveArquivotxt.escreveTexto(f'\nTempo de ordenação base Editoras: {tempoEditoramerge:.6f}')
    escreveArquivotxt.escreveTexto(f'\nTempo de ordenação base Livros: {tempoLivromerge:.6f}')
    # Escrevendo a base de dados ORDENADA no arquivo bin
    escreveArquivobin.escreveTexto(f'{20*"="}Base ORDENADA{20*"="}\n')
    escreveArquivobin.escreveLista(livros)
    escreveArquivobin.escreveLista(autores)
    escreveArquivobin.escreveLista(editoras)
    escreveArquivobin.escreveTexto(f'Tempo de ordenação base Autores: {tempoAutormerge:.6f}')
    escreveArquivobin.escreveTexto(f'\nTempo de ordenação base Editoras: {tempoEditoramerge:.6f}')
    escreveArquivobin.escreveTexto(f'\nTempo de ordenação base Livros: {tempoLivromerge:.6f}')

    # ====================================PESQUISANDO NA BASE LIVROS====================================
    idProcurado = int(input('Id a ser procurado na base de livros: '))
    escrevePesquisatxt.escreveTexto(f'{44 * "="}\n')
    escrevePesquisatxt.escreveTexto(f'Procurando ID------>[{idProcurado}]:\n')
    escrevePesquisatxt.escreveTexto(f'{24 * "="}\n')
    iPBin = time.time()
    pLivroID_bin, pLivroCont_bin, pLivroBigO_bin = Pesquisas.pesquisa_binaria(livros, idProcurado)
    fPbin = time.time()
    iPseq = time.time()
    pLivroID_seq, pLivroCont_seq, pLivroBigO_seq = Pesquisas.pesquisa_sequencial(livros, idProcurado)
    fPseq = time.time()
    tempoPbin = fPbin - iPBin
    tempoPsequ = fPseq - iPseq
    escrevePesquisatxt.escreveTexto(f'Pesquisa Binaria: \n')
    escrevePesquisatxt.escreveItem(livros, pLivroID_bin)
    escrevePesquisatxt.escreveTexto(f'BigO: {math.ceil(pLivroBigO_bin)}')
    escrevePesquisatxt.escreveTexto(f'\nExecuções: {pLivroCont_bin}')
    escrevePesquisatxt.escreveTexto(f'\nTempo: {tempoPsequ:.6f}s\n')
    escrevePesquisatxt.escreveTexto(f'\nPesquisa Sequencial:\n')
    escrevePesquisatxt.escreveItem(livros, pLivroID_seq)
    escrevePesquisatxt.escreveTexto(f'BigO: {math.ceil(pLivroBigO_seq)}')
    escrevePesquisatxt.escreveTexto(f'\nExecuções: {pLivroCont_seq}')
    escrevePesquisatxt.escreveTexto(f'\nTempo: {tempoPsequ:.6f}s\n')
    escrevePesquisatxt.escreveTexto(f'{44*"="}\n\n')

