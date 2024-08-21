from faker import Faker
import struct
import os
import math
import time
import random


class Editora:
    def __init__(self):
        self.id = None
        self.nome = ''
        self.pais = ''
        self.contato = ''
        self.fake = Faker()
        self.caminhocompleto = os.path.join("Bases_dat", "Editoras.dat")
        self.caminho_txt = os.path.join("Bases_dat", "Pesquisas.txt")

    def gerador(self, tamanho):
        os.makedirs("Bases_dat", exist_ok=True)
        with open(self.caminhocompleto, 'wb') as arquivo_binario:
            for i in range(tamanho):
                self.id = i + 1
                self.nome = self.fake.company()
                self.pais = self.fake.country()
                self.contato = self.fake.phone_number()

                idbinario = struct.pack('i', self.id)
                nome_binario = self.nome.encode('utf-8')
                pais_binario = self.pais.encode('utf-8')
                contato_binario = self.contato.encode('utf-8')

                arquivo_binario.write(idbinario)
                arquivo_binario.write(nome_binario.ljust(100, b'\x00'))
                arquivo_binario.write(pais_binario.ljust(100, b'\x00'))
                arquivo_binario.write(contato_binario.ljust(100, b'\x00'))
        print(f'{50 * "-"}')
        print(f'Base de editoras  gerada com sucesso! Tam----> [{tamanho}]')
        self.embaralhar_base()
        print(f'{50 * "-"}')

    def pesquisa_binaria(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para pesquisa binária!!')
            return

        tamanho_registro = 4 + 100 + 100 + 100

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
                    nome_binario = arquivo_binario.read(100).rstrip(b'\x00')
                    nome = nome_binario.decode('utf-8')
                    pais_binario = arquivo_binario.read(100).rstrip(b'\x00')
                    pais = pais_binario.decode('utf-8')
                    contato_binario = arquivo_binario.read(100).rstrip(b'\x00')
                    contato = contato_binario.decode('utf-8')
                    print(f'\n{20 * "="}Pesquisa binária concluida{20 * "="} ')
                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(f"Editora: [{id_meio}] Nome: {nome}, Pais: {pais}, Contato: {contato}\n")

                    print(f"Editora [{id_meio}] gravada no arquivo '{self.caminho_txt}' com sucesso!")
                    print(f'Big0(pior caso): {math.ceil(big_o)}')
                    print(f'Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                    print(f'{60 * "-"}')
                    return

                if id_meio > id_procurado:
                    alto = meio - 1
                else:
                    baixo = meio + 1

            print('Editora não Existe!')
            with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Editora não existe')
            return

    def pesquisa_sequencial(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para pesquisa sequêncial!!')
            return

        tamanho_registro = 4 + 50 + 50 + 50
        count = 0

        with open(self.caminhocompleto, 'rb') as arquivo_binario:
            arquivo_binario.seek(0, os.SEEK_END)
            num_registros = arquivo_binario.tell() // tamanho_registro
            arquivo_binario.seek(0)

            while True:

                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break
                id_registro = struct.unpack('i', id_binario)[0]
                nome_binario = arquivo_binario.read(100).rstrip(b'\x00')
                nome = nome_binario.decode('utf-8')
                pais_binario = arquivo_binario.read(100).rstrip(b'\x00')
                pais = pais_binario.decode('utf-8')
                contato_binario = arquivo_binario.read(100).rstrip(b'\x00')
                contato = contato_binario.decode('utf-8')
                count += 1

                if id_registro == id_procurado:
                    temp_Final = time.time()
                    print(f'\n{20 * "="}Pesquisa sequencial concluida{20 * "="} ')
                    with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write(f"Autor: [{id_registro}] Nome: {nome}, Pais: {pais}, Contato: {contato}\n")

                        print(f"Editora [{id_registro}] gravada no arquivo '{self.caminho_txt}' com sucesso!")
                        print(f'Big0(pior caso): {num_registros}')
                        print(f'Execuções: {count}')
                        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                        print(f'{60 * "-"}')
                        return

            print('Editora não encontrada!')
            with open(self.caminho_txt, 'w', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Editora não encontrada!')

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
                nome_binario = arquivo_binario.read(100).rstrip(b'\x00')  # 50 bytes para o nome
                nome = nome_binario.decode('utf-8')
                pais_binario = arquivo_binario.read(100).rstrip(b'\x00')  # 20 bytes para o país
                pais = pais_binario.decode('utf-8')
                contato_binario = arquivo_binario.read(100).rstrip(b'\x00')  # 20 bytes para o contato
                contato = contato_binario.decode('utf-8')

                print(f"ID: {id}, Nome: {nome}, País: {pais}, Contato: {contato}")

    def embaralhar_base(self):
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para embaralhamento!')
            return

        tamanho_nome = 100
        tamanho_pais = 100
        tamanho_contato = 100
        tamanho_registro = 4 + tamanho_nome + tamanho_pais + tamanho_contato

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
        print(f'Base de editoras embaralhada com sucesso!')
        os.remove(backup_file_path)

    def bubble_sort_base(self):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para ordenação!')
            return

        tamanho_nome = 100
        tamanho_pais = 100
        tamanho_contato = 100
        tamanho_registro = 4 + tamanho_nome + tamanho_pais + tamanho_contato
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
        print('Base de editoras ordenada com sucesso usando Bubble Sort!')
        print(f'Numero de comparações: {comparacoes}')
        print(f'Numero de trocas: {trocas}')
        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
        print(f'{60 * "-"}')
        return
