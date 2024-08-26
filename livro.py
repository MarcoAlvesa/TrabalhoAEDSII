from faker import Faker
import struct
import os
import random
import time
import math
from autor import Autor
from editora import Editora


class Livro:
    def __init__(self):
        self.editora_id = None
        self.editora_nome = None
        self.autor_id = None
        self.autor_nome = None
        self.id = None
        self.titulo = ''
        self.autor = ''
        self.editora = ''
        self.anoPubli = ''
        self.fake = Faker()
        self.caminho_livros = os.path.join("Bases_dat", "Livros.dat")
        self.caminho_autores = os.path.join("Bases_dat", "Autores.dat")
        self.caminho_editoras = os.path.join("Bases_dat", "Editoras.dat")
        self.caminho_txt = os.path.join("Bases_dat", "Pesquisas.txt")
        self.formato_autor = 'i50s10s'
        self.formato_editora = 'i150s150s30s'
        if os.path.exists(self.caminho_txt):
            os.remove(self.caminho_txt)

    def gerador(self, tamanho):
        t_inicio = time.time()
        os.makedirs("Bases_dat", exist_ok=True)

        with open(self.caminho_livros, 'wb') as arquivo_binario:
            for i in range(tamanho):
                self.id = i + 1
                self.titulo = self.fake.sentence(nb_words=4)

                # Tamanhos dos registros binários
                tamanho_registro_autor = struct.calcsize(self.formato_autor)
                tamanho_registro_editora = struct.calcsize(self.formato_editora)

                # Obter um autor e uma editora aleatórios
                registro_autor = self.obter_registro_aleatorio(self.caminho_autores, tamanho_registro_autor)
                registro_editora = self.obter_registro_aleatorio(self.caminho_editoras, tamanho_registro_editora)

                # Desempacotar os registros
                autor_desempacotado = struct.unpack(self.formato_autor, registro_autor)
                editora_desempacotada = struct.unpack(self.formato_editora, registro_editora)

                # Extrair e limpar os dados de autor
                autor_id = autor_desempacotado[0]
                autor_nome = autor_desempacotado[1].decode('utf-8').rstrip('\x00').strip()
                self.autor_id = autor_id
                self.autor_nome = autor_nome

                # Extrair e limpar os dados de editora
                editora_id = editora_desempacotada[0]
                editora_nome = editora_desempacotada[1].decode('utf-8').rstrip('\x00').strip()
                self.editora_id = editora_id
                self.editora_nome = editora_nome

                # Gerar um ano de publicação aleatório
                self.anoPubli = random.randint(1900, 2024)

                # Empacotar os dados para escrita no arquivo binário
                id_binario = struct.pack('i', self.id)
                titulo_binario = self.titulo.encode('utf-8').ljust(150, b'\x00')
                autor_binario = struct.pack('i50s', self.autor_id, self.autor_nome.encode('utf-8').ljust(50, b'\x00'))
                editora_binario = struct.pack('i150s', self.editora_id,
                                              self.editora_nome.encode('utf-8').ljust(150, b'\x00'))
                ano_publi_binario = struct.pack('i', self.anoPubli)

                # Escrever no arquivo binário
                arquivo_binario.write(id_binario)
                arquivo_binario.write(titulo_binario)
                arquivo_binario.write(autor_binario)
                arquivo_binario.write(editora_binario)
                arquivo_binario.write(ano_publi_binario)
        t_final = time.time()
        print(f'Base: [livros] gerada com sucesso! Tam -> [{tamanho}]')
        print(f'Tempo: {t_final - t_inicio:.2f}s ')
        self.embaralhar_base()
        print(f'{50 * "-"}')

    def printBase(self):
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para exibir informações!')
            return

        import struct

        with open(self.caminho_livros, 'rb') as arquivo_binario:
            while True:
                # Ler 4 bytes para o ID do livro
                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break  # Se não há mais dados, sair do loop
                id_livro = struct.unpack('i', id_binario)[0]

                # Ler 150 bytes para o título
                titulo_binario = arquivo_binario.read(150)
                titulo = titulo_binario.decode('utf-8').rstrip('\x00').strip()

                # Ler 4 bytes para o ID do autor
                autor_id_binario = arquivo_binario.read(4)
                autor_id = struct.unpack('i', autor_id_binario)[0]

                # Ler 50 bytes para o nome do autor
                autor_nome_binario = arquivo_binario.read(50)
                autor_nome = autor_nome_binario.decode('utf-8').rstrip('\x00').strip()

                # Ler 4 bytes para o ID da editora
                editora_id_binario = arquivo_binario.read(4)
                editora_id = struct.unpack('i', editora_id_binario)[0]

                # Ler 150 bytes para o nome da editora
                editora_nome_binario = arquivo_binario.read(150)
                editora_nome = editora_nome_binario.decode('utf-8').rstrip('\x00').strip()

                # Ler 4 bytes para o ano de publicação
                ano_publi_binario = arquivo_binario.read(4)
                ano_publi = struct.unpack('i', ano_publi_binario)[0]

                # Exibir os dados
                print(f'Livro: [{id_livro}] Titulo: {titulo}, Autor: [{autor_id}] {autor_nome}, Editora : [{editora_id}'
                      f'] {editora_nome}, Ano de publicação: {ano_publi}')
        print(f'{50 * "-"}')


    def pesquisa_binaria(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para pesquisa binária!!')
            return

        # Definição dos tamanhos dos campos
        TAMANHO_TITULO = 150
        TAMANHO_AUTOR = 54  # 4 bytes para ID + 50 bytes para Nome
        TAMANHO_EDITORA = 154  # 4 bytes para ID + 150 bytes para Nome
        TAMANHO_ANO_PUBLI = 4
        tamanho_registro = 4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA + TAMANHO_ANO_PUBLI

        with open(self.caminho_livros, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)
            num_registros = arquivo_binario.tell() // tamanho_registro

            baixo = 0
            alto = num_registros - 1
            count = 0

            while baixo <= alto:
                count += 1
                meio = (baixo + alto) // 2
                posicao = meio * tamanho_registro

                arquivo_binario.seek(posicao)
                id_binario = arquivo_binario.read(4)
                id_meio = struct.unpack('i', id_binario)[0]

                if id_meio == id_procurado:
                    temp_Final = time.time()

                    # Ler e processar o título
                    titulo_binario = arquivo_binario.read(TAMANHO_TITULO).rstrip(b'\x00')
                    titulo = titulo_binario.decode('utf-8', errors='ignore').strip()

                    # Ler e processar o autor
                    autor_binario = arquivo_binario.read(TAMANHO_AUTOR)
                    autor_id, autor_nome_binario = struct.unpack('i50s', autor_binario)
                    autor_nome = autor_nome_binario.decode('utf-8').rstrip('\x00').strip()

                    # Ler e processar a editora
                    editora_binario = arquivo_binario.read(TAMANHO_EDITORA)
                    editora_id, editora_nome_binario = struct.unpack('i150s', editora_binario)
                    editora_nome = editora_nome_binario.decode('utf-8').rstrip('\x00').strip()

                    # Ler e processar o ano de publicação
                    ano_publi_binario = arquivo_binario.read(TAMANHO_ANO_PUBLI)
                    ano_publi = struct.unpack('i', ano_publi_binario)[0]

                    # Gravar dados no arquivo texto
                    with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write('Pesquisa binária base [Livro]: \n')
                        arquivo_txt.write(
                            f"Livro: {id_meio}\nTítulo: {titulo}\nAutor: [{autor_id}]-> {autor_nome}\nEditora: [{editora_id}]-> {editora_nome}\nAno de Publicação: {ano_publi}\n{50*'='}\n"
                        )

                    print(f'\n{20 * "="}Pesquisa binária concluída{20 * "="}')
                    print(f"Livro [{id_meio}] gravado no arquivo: '{self.caminho_txt}' com sucesso!")
                    print(f'Big0(pior caso): {math.ceil(math.log2(num_registros))} | Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial):.6f}s')
                    print(f'{60 * "-"}')
                    return

                if id_meio > id_procurado:
                    alto = meio - 1
                else:
                    baixo = meio + 1

            print('Livro não encontrado!')
            with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Livro não encontrado!')

    def pesquisa_sequencial(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para pesquisa sequencial!!')
            return

        # Definição dos tamanhos dos campos
        TAMANHO_TITULO = 150
        TAMANHO_AUTOR = 54  # 4 bytes para ID + 50 bytes para Nome
        TAMANHO_EDITORA = 154  # 4 bytes para ID + 150 bytes para Nome
        TAMANHO_ANO_PUBLI = 4
        tamanho_registro = 4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA + TAMANHO_ANO_PUBLI
        count = 0

        with open(self.caminho_livros, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)
            num_registros = arquivo_binario.tell() // tamanho_registro
            arquivo_binario.seek(0)

            while True:
                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break

                id_registro = struct.unpack('i', id_binario)[0]
                titulo_binario = arquivo_binario.read(TAMANHO_TITULO).rstrip(b'\x00')
                autor_binario = arquivo_binario.read(TAMANHO_AUTOR)
                editora_binario = arquivo_binario.read(TAMANHO_EDITORA)
                anoPubli_binario = arquivo_binario.read(TAMANHO_ANO_PUBLI)

                titulo = titulo_binario.decode('utf-8', errors='ignore').strip()

                # Desempacotar e processar o autor
                autor_id, autor_nome_binario = struct.unpack('i50s', autor_binario)
                autor_nome = autor_nome_binario.decode('utf-8').rstrip('\x00').strip()

                # Desempacotar e processar a editora
                editora_id, editora_nome_binario = struct.unpack('i150s', editora_binario)
                editora_nome = editora_nome_binario.decode('utf-8').rstrip('\x00').strip()

                ano_publi = struct.unpack('i', anoPubli_binario)[0]

                count += 1

                if id_registro == id_procurado:
                    temp_Final = time.time()
                    with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write('Pesquisa sequencial base [Livro]:\n')
                        arquivo_txt.write(
                            f"Livro: {id_registro}\nTítulo: {titulo}\nAutor: [{autor_id}]-> {autor_nome}\nEditora: [{editora_id}]-> {editora_nome}\nAno de Publicação: {ano_publi}\n{50*'='}\n"
                        )

                    print(f'\n{20 * "="}Pesquisa sequencial concluída{20 * "="}')
                    print(f"Livro [{id_registro}] gravado no arquivo: '{self.caminho_txt}' com sucesso!")
                    print(f'Big0(pior caso): {math.ceil(num_registros)} | Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial):.6f}s')
                    print(f'{60 * "-"}')
                    return

        print('Livro não encontrado!')
        with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
            arquivo_txt.write('Livro não encontrado!')

    def embaralhar_base(self):
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para embaralhamento!')
            return

        TAMANHO_TITULO = 150
        TAMANHO_AUTOR = 54  # 4 bytes para ID + 50 bytes para Nome
        TAMANHO_EDITORA = 154  # 4 bytes para ID + 150 bytes para Nome
        TAMANHO_ANO_PUBLI = 4
        tamanho_registro = 4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA + TAMANHO_ANO_PUBLI

        temp_file_path = self.caminho_livros + ".shuffled"

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        backup_file_path = self.caminho_livros + ".backup"
        if os.path.exists(backup_file_path):
            os.remove(backup_file_path)
        os.rename(self.caminho_livros, backup_file_path)

        with open(backup_file_path, 'rb') as arquivo:
            arquivo.seek(0, os.SEEK_END)
            tamanho_arquivo = arquivo.tell()
            num_registros = tamanho_arquivo // tamanho_registro

            indices = list(range(num_registros))
            random.shuffle(indices)

            with open(temp_file_path, 'wb') as temp_file:
                for i in indices:
                    posicao = i * tamanho_registro
                    arquivo.seek(posicao)
                    registro = arquivo.read(tamanho_registro)
                    temp_file.write(registro)

        os.rename(temp_file_path, self.caminho_livros)
        print(f'Base: [livros] embaralhada com sucesso!')
        os.remove(backup_file_path)

    def bubble_sort_base(self):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para ordenação!')
            return

        TAMANHO_TITULO = 150
        TAMANHO_AUTOR = 54  # 4 bytes para ID + 50 bytes para Nome
        TAMANHO_EDITORA = 154  # 4 bytes para ID + 150 bytes para Nome
        TAMANHO_ANO_PUBLI = 4
        tamanho_registro = 4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA + TAMANHO_ANO_PUBLI

        comparacoes = 0
        trocas = 0
        with open(self.caminho_livros, 'r+b') as arquivo:
            arquivo.seek(0, os.SEEK_END)
            tamanho_arquivo = arquivo.tell()
            num_registros = tamanho_arquivo // tamanho_registro

            for i in range(num_registros):
                # Indicador de se houve trocas
                trocou = False
                for j in range(0, num_registros - i - 1):
                    # Posição dos registros adjacentes
                    pos_atual = j * tamanho_registro
                    pos_proximo = (j + 1) * tamanho_registro

                    # Ler os dois registros
                    arquivo.seek(pos_atual)
                    registro_atual = arquivo.read(tamanho_registro)
                    id_atual = struct.unpack('i', registro_atual[:4])[0]

                    arquivo.seek(pos_proximo)
                    registro_proximo = arquivo.read(tamanho_registro)
                    id_proximo = struct.unpack('i', registro_proximo[:4])[0]

                    comparacoes += 1
                    # Comparar e trocar se necessário
                    if id_atual > id_proximo:
                        arquivo.seek(pos_atual)
                        arquivo.write(registro_proximo)

                        arquivo.seek(pos_proximo)
                        arquivo.write(registro_atual)
                        trocas += 1
                        trocou = True

                # Se não houve trocas, a lista já está ordenada
                if not trocou:
                    break
        temp_Final = time.time()
        print(f'{60 * "-"}')
        print(f'Base: [livros] ordenada com sucesso usando Bubble Sort.\n')
        print(f'Numero de comparações: {comparacoes}')
        print(f'Numero de trocas: {trocas}')
        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
        return

    @staticmethod
    def obter_registro_aleatorio(caminho, tamanho_registro):
        with open(caminho, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)  # Vai para o final do arquivo
            tamanho_arquivo = arquivo_binario.tell()
            num_registros = tamanho_arquivo // tamanho_registro

            # Escolhe um registro aleatório
            indice_aleatorio = random.randint(0, num_registros - 1)
            posicao = indice_aleatorio * tamanho_registro

            arquivo_binario.seek(posicao)
            registro = arquivo_binario.read(tamanho_registro)

        return registro
