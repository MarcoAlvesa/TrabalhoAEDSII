from faker import Faker
import struct
import os
import random
import time
import math


class Livro:
    def __init__(self):
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
        if os.path.exists(self.caminho_txt):
            os.remove(self.caminho_txt)

    def gerador(self, tamanho):
        os.makedirs("Bases_dat", exist_ok=True)

        with open(self.caminho_livros, 'wb') as arquivo_binario:
            for i in range(tamanho):
                self.id = i + 1
                self.titulo = self.fake.sentence(nb_words=4)

                # Formatos dos registros binários de autores e editoras
                formato_autor = 'i50s10s'  # ID, Nome (50 bytes), DataNasc (10 bytes)
                formato_editora = 'i100s100s100s'  # ID, Nome (50 bytes)

                # Tamanhos dos registros binários
                tamanho_registro_autor = struct.calcsize(formato_autor)
                tamanho_registro_editora = struct.calcsize(formato_editora)

                # Obter um autor e uma editora aleatórios
                registro_autor = obter_registro_aleatorio(self.caminho_autores, tamanho_registro_autor)
                registro_editora = obter_registro_aleatorio(self.caminho_editoras, tamanho_registro_editora)

                autor_desempacotado = struct.unpack(formato_autor, registro_autor)
                editora_desempacotada = struct.unpack(formato_editora, registro_editora)

                autor_id = autor_desempacotado[0]
                self.autor = '{} - {}'.format(autor_id, autor_desempacotado[1].decode('utf-8').strip('\x00'))

                editora_id = editora_desempacotada[0]
                self.editora = '{} - {}'.format(editora_id, editora_desempacotada[1].decode('utf-8').strip('\x00'))

                self.anoPubli = random.randint(1900, 2024)

                idbinario = struct.pack('i', self.id)
                titulo_binario = self.titulo.encode('utf-8')
                autor_binario = self.autor.encode('utf-8')
                editora_binario = self.editora.encode('utf-8')
                anoPubli_binario = struct.pack('i', self.anoPubli)  # Corrigido para empacotar como inteiro

                # Escrever no arquivo binário de livros
                arquivo_binario.write(idbinario)
                arquivo_binario.write(titulo_binario.ljust(50, b'\x00'))
                arquivo_binario.write(autor_binario.ljust(64, b'\x00'))
                arquivo_binario.write(editora_binario.ljust(304, b'\x00'))
                arquivo_binario.write(anoPubli_binario)

        print(f'{50 * "-"}')
        print(f'Base de livros gerada com sucesso! Tam----> [{tamanho}]')
        print(f'{50 * "-"}')

    def printBase(self):
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para exibir informações!')
            return

        # Definição dos tamanhos dos campos
        TAMANHO_TITULO = 50
        TAMANHO_AUTOR = 64
        TAMANHO_EDITORA = 304
        TAMANHO_ANO_PUBLI = 4  # O ano de publicação é um inteiro e ocupa 4 bytes

        tamanho_registro = 4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA + TAMANHO_ANO_PUBLI

        with open(self.caminho_livros, 'rb') as arquivo_binario:
            while True:
                registro_binario = arquivo_binario.read(tamanho_registro)
                if not registro_binario:
                    break

                # Verificar se o registro lido tem o tamanho esperado
                if len(registro_binario) < tamanho_registro:
                    print("Registro com tamanho inesperado encontrado, possivelmente corrompido.")
                    continue

                # Desempacotar o registro
                try:
                    id = struct.unpack('i', registro_binario[:4])[0]
                    titulo_binario = registro_binario[4:4 + TAMANHO_TITULO].rstrip(b'\x00')
                    autor_binario = registro_binario[4 + TAMANHO_TITULO:4 + TAMANHO_TITULO + TAMANHO_AUTOR].rstrip(
                        b'\x00')
                    editora_binario = registro_binario[
                                      4 + TAMANHO_TITULO + TAMANHO_AUTOR:4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA].rstrip(
                        b'\x00')
                    anoPubli_binario = \
                        struct.unpack('i', registro_binario[4 + TAMANHO_TITULO + TAMANHO_AUTOR + TAMANHO_EDITORA:])[0]

                    # Decodifica os campos
                    titulo = titulo_binario.decode('utf-8', errors='ignore')
                    autor = autor_binario.decode('utf-8', errors='ignore')
                    editora = editora_binario.decode('utf-8', errors='ignore')
                    anoPubli = anoPubli_binario

                    # Exibe as informações
                    print(
                        f"ID: {id}, Título: {titulo}, Autor: {autor}, Editora: {editora}, Ano de Publicação: {anoPubli}")

                except struct.error as e:
                    print(f"Erro ao desempacotar o registro: {e}")
                    continue

    def pesquisa_binaria(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para pesquisa binária!!')
            return

        # Definição dos tamanhos dos campos
        TAMANHO_TITULO = 50
        TAMANHO_AUTOR = 50
        TAMANHO_EDITORA = 50
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
                    titulo_binario = arquivo_binario.read(TAMANHO_TITULO).rstrip(b'\x00')
                    autor_binario = arquivo_binario.read(TAMANHO_AUTOR).rstrip(b'\x00')
                    editora_binario = arquivo_binario.read(TAMANHO_EDITORA).rstrip(b'\x00')
                    anoPubli_binario = arquivo_binario.read(TAMANHO_ANO_PUBLI)

                    titulo = titulo_binario.decode('utf-8', errors='ignore').strip()
                    autor = autor_binario.decode('utf-8', errors='ignore').strip()
                    editora = editora_binario.decode('utf-8', errors='ignore').strip()
                    anoPubli = struct.unpack('i', anoPubli_binario)[0]

                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(
                            f"Livro ID: [{id_meio}] Título: {titulo}, Autor: {autor}, Editora: {editora}, Ano de Publicação: {anoPubli}\n")

                    print(f'\n{20 * "="}Pesquisa binária concluída{20 * "="} ')
                    print(f"Livro [{id_meio}] gravado no arquivo '{self.caminho_txt}' com sucesso!")
                    print(f'Big O (pior caso): {math.ceil(math.log2(num_registros))}')
                    print(f'Execuções: {count}')
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
        TAMANHO_TITULO = 50
        TAMANHO_AUTOR = 50
        TAMANHO_EDITORA = 50
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
                autor_binario = arquivo_binario.read(TAMANHO_AUTOR).rstrip(b'\x00')
                editora_binario = arquivo_binario.read(TAMANHO_EDITORA).rstrip(b'\x00')
                anoPubli_binario = arquivo_binario.read(TAMANHO_ANO_PUBLI)

                titulo = titulo_binario.decode('utf-8', errors='ignore').strip()
                autor = autor_binario.decode('utf-8', errors='ignore').strip()
                editora = editora_binario.decode('utf-8', errors='ignore').strip()
                anoPubli = struct.unpack('i', anoPubli_binario)[0]

                count += 1

                if id_registro == id_procurado:
                    temp_Final = time.time()
                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(
                            f"Livro ID: [{id_registro}] Título: {titulo}, Autor: {autor}, Editora: {editora}, Ano de Publicação: {anoPubli}\n")

                    print(f'\n{20 * "="}Pesquisa sequencial concluída{20 * "="} ')
                    print(f"Livro [{id_registro}] gravado no arquivo '{self.caminho_txt}' com sucesso!")
                    print(f'Big O (pior caso): {num_registros}')
                    print(f'Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial):.6f}s')
                    print(f'{60 * "-"}')
                    return

            print('Livro não encontrado!')
            with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Livro não encontrado!')

    def embaralhar_base(self):
        if not os.path.exists(self.caminho_livros):
            print(f'Base "{self.caminho_livros}" não encontrada para embaralhamento!')
            return

        TAMANHO_TITULO = 50
        TAMANHO_AUTOR = 50
        TAMANHO_EDITORA = 50
        TAMANHO_ANO_PUBLI = 4  # O ano de publicação é um inteiro e ocupa 4 bytes
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
        print(f'Base de livros embaralhada com sucesso!')
        os.remove(backup_file_path)


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
