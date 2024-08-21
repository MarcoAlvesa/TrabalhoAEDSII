import random
from faker import Faker
import struct
import os
import math
import time


class Autor:
    def __init__(self):
        self.id = None
        self.nome = ''
        self.datanasc = ''
        self.fake = Faker()
        self.caminhocompleto = os.path.join("Bases_dat", "Autores.dat")
        self.caminho_txt = os.path.join("Bases_dat", "Pesquisas.txt")

    def gerador(self, tamanho):
        os.makedirs("Bases_dat", exist_ok=True)
        with open(self.caminhocompleto, 'wb') as arquivo_binario:
            for i in range(tamanho):
                self.id = i + 1
                self.nome = self.fake.name()
                self.datanasc = self.fake.date_of_birth(minimum_age=20, maximum_age=90).strftime('%d/%m/%Y')

                idbinario = struct.pack('i', self.id)
                nome_binario = self.nome.encode('utf-8')
                datanasc_binario = self.datanasc.encode('utf-8')

                arquivo_binario.write(idbinario)
                arquivo_binario.write(nome_binario.ljust(50, b'\x00'))
                arquivo_binario.write(datanasc_binario.ljust(10, b'\x00'))
        print(f'{50 * "-"}')
        print(f'Base de autores  gerada com sucesso! Tam----> [{tamanho}]')
        self.embaralhar_base()
        print(f'{50 * "-"}')

    def pesquisa_binaria(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para pesquisa binária!!')
            return

        tamanho_registro = 4 + 50 + 10

        with open(self.caminhocompleto, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)
            num_registros = arquivo_binario.tell() // tamanho_registro

            alto = num_registros - 1
            big_o = math.log2(num_registros)
            count = 0
            baixo = 0

            while baixo <= alto:
                count += 1
                meio = (baixo + alto) // 2
                posicao = meio * tamanho_registro

                arquivo_binario.seek(posicao)
                id_binario = arquivo_binario.read(4)
                id_meio = struct.unpack('i', id_binario)[0]
                if id_meio == id_procurado:
                    temp_Final = time.time()
                    nome_binario = arquivo_binario.read(50).rstrip(b'\x00')
                    nome = nome_binario.decode('utf-8')
                    datanasc_binario = arquivo_binario.read(10).rstrip(b'\x00')
                    datanasc = datanasc_binario.decode('utf-8')

                    print(f'\n{20 * "="}Pesquisa binária concluida{20 * "="} ')
                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(f"Autor: [{id_meio}] Nome: {nome}, Data de nascimento: {datanasc}\n")

                    print(f"Autor [{id_meio}] gravado no arquivo '{self.caminho_txt}' com sucesso!")
                    print(f'Big0(pior caso): {math.ceil(big_o)}')
                    print(f'Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                    print(f'{60 * "-"}')
                    return

                if id_meio > id_procurado:
                    alto = meio - 1
                else:
                    baixo = meio + 1

        print('Autor não Existe!')
        with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
            arquivo_txt.write('Autor não existe')
        return

    def pesquisa_sequencial(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para pesquisa sequêncial!!')
            return

        tamanho_registro = 4 + 50 + 10

        with open(self.caminhocompleto, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)
            num_registros = arquivo_binario.tell() // tamanho_registro
            arquivo_binario.seek(0)
            count = 0

            while True:

                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break
                id_registro = struct.unpack('i', id_binario)[0]
                nome_binario = arquivo_binario.read(50).rstrip(b'\x00')
                nome = nome_binario.decode('utf-8')
                datanasc_binario = arquivo_binario.read(10).rstrip(b'\x00')
                datanasc = datanasc_binario.decode('utf-8')
                count += 1

                if id_registro == id_procurado:
                    temp_Final = time.time()
                    print(f'\n{20 * "="}Pesquisa sequencial concluida{20 * "="} ')
                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(f"Autor: [{id_registro}] Nome: {nome}, Data de nascimento: {datanasc}\n")

                        print(f"Autor [{id_registro}] gravado no arquivo '{self.caminho_txt}' com sucesso!")
                        print(f'Big0(pior caso): {num_registros}')
                        print(f'Execuções: {count}')
                        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                        print(f'{60 * "-"}')
                        return

            print('Autor não encontrado!')
            with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Autor não encontrado')

    def printBase(self):
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para exibir informações!')
            return
        with open(self.caminhocompleto, 'rb') as arquivo_binario:
            while True:
                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break

                id = struct.unpack('i', id_binario)[0]
                nome_binario = arquivo_binario.read(50).rstrip(b'\x00')  # 50 bytes para o nome
                nome = nome_binario.decode('utf-8')
                datanasc_binario = arquivo_binario.read(10).rstrip(b'\x00')  # 10 bytes para a data de nascimento
                datanasc = datanasc_binario.decode('utf-8')

                print(f"ID: {id}, Nome: {nome}, Data de Nascimento: {datanasc}")

    def embaralhar_base(self):
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para embaralhamento!')
            return

        tamanho_nome = 50
        tamanho_datanasc = 10
        tamanho_registro = 4 + tamanho_nome + tamanho_datanasc

        temp_file_path = self.caminhocompleto + ".shuffled"

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        backup_file_path = self.caminhocompleto + ".backup"
        if os.path.exists(backup_file_path):
            os.remove(backup_file_path)
        os.rename(self.caminhocompleto, backup_file_path)

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

        os.rename(temp_file_path, self.caminhocompleto)
        print(f'Base de Autores embaralhada com sucesso!')
        os.remove(backup_file_path)

    def bubble_sort_base(self):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para ordenação!')
            return

        tamanho_nome = 50
        tamanho_datanasc = 10
        tamanho_registro = 4 + tamanho_nome + tamanho_datanasc  # 4 bytes para ID, 50 para nome, 10 para data de nascimento
        comparacoes = 0
        trocas = 0
        with open(self.caminhocompleto, 'r+b') as arquivo:
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
        print(f'{20*"="}Base de Autores ordenada com sucesso usando Bubble Sort{20*"="}')
        print(f'Numero de comparações: {comparacoes}')
        print(f'Numero de trocas: {trocas}')
        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
        print(f'{60 * "-"}')
        return
