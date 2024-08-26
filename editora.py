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
        t_inicial = time.time()
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
                arquivo_binario.write(nome_binario.ljust(150, b'\x00'))
                arquivo_binario.write(pais_binario.ljust(150, b'\x00'))
                arquivo_binario.write(contato_binario.ljust(30, b'\x00'))
        t_final = time.time()
        print(f'Base: [editoras] gerada com sucesso! Tam -> [{tamanho}]')
        print(f'Tempo: {t_final - t_inicial:.2f}s ')
        self.embaralhar_base()
        print(f'{50 * "-"}')
    def printBase(self):
        if not os.path.exists(self.caminhocompleto):
            print(f'Base: "{self.caminhocompleto}" não encontrada para exibir informações!')
            return

        with open(self.caminhocompleto, 'rb') as arquivo_binario:
            while True:
                id_binario = arquivo_binario.read(4)
                if not id_binario:
                    break

                id = struct.unpack('i', id_binario)[0]
                nome_binario = arquivo_binario.read(150).rstrip(b'\x00')  # 50 bytes para o nome
                nome = nome_binario.decode('utf-8')
                pais_binario = arquivo_binario.read(150).rstrip(b'\x00')  # 50 bytes para o país
                pais = pais_binario.decode('utf-8')
                contato_binario = arquivo_binario.read(30).rstrip(b'\x00')  # 50 bytes para o contato
                contato = contato_binario.decode('utf-8')

                print(f"Editora: [{id}] Nome: {nome}, País: {pais}, Contato: {contato}")
        print(f'{50 * "-"}')
    def pesquisa_binaria(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Pesquisa binária: Base "{self.caminhocompleto}" não encontrada para pesquisa binária!!')
            return

        tamanho_registro = 4 + 150 + 150 + 30

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
                    nome_binario = arquivo_binario.read(150).rstrip(b'\x00')
                    nome = nome_binario.decode('utf-8')
                    pais_binario = arquivo_binario.read(150).rstrip(b'\x00')
                    pais = pais_binario.decode('utf-8')
                    contato_binario = arquivo_binario.read(30).rstrip(b'\x00')
                    contato = contato_binario.decode('utf-8')
                    print(f'\n{20 * "="}Pesquisa binária concluida{20 * "="} ')
                    with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write('Pesquisa binária base [Editora]:\n')
                        arquivo_txt.write(f"Editora: {id_meio}\nNome: {nome}\nPais: {pais}\nContato: {contato}\n{50*'='}\n")

                    print(f"Editora [{id_meio}] gravada no arquivo: '{self.caminho_txt}' com sucesso!")
                    print(f'Big0(pior caso): {math.ceil(big_o)} | Execuções: {count}')
                    print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                    print(f'{60 * "-"}')
                    return

                if id_meio > id_procurado:
                    alto = meio - 1
                else:
                    baixo = meio + 1

            print('Pesquisa binária: Editora não existe!')
            with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Pesquisa binária: Editora não existe')
            return
    def pesquisa_sequencial(self, id_procurado):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Pesquisa sequencial: Base "{self.caminhocompleto}" não encontrada para pesquisa sequêncial!!')
            return

        tamanho_registro = 4 + 150 + 150 + 30
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
                nome_binario = arquivo_binario.read(150).rstrip(b'\x00')
                nome = nome_binario.decode('utf-8')
                pais_binario = arquivo_binario.read(150).rstrip(b'\x00')
                pais = pais_binario.decode('utf-8')
                contato_binario = arquivo_binario.read(30).rstrip(b'\x00')
                contato = contato_binario.decode('utf-8')
                count += 1

                if id_registro == id_procurado:
                    temp_Final = time.time()
                    print(f'\n{20 * "="}Pesquisa sequencial concluida{20 * "="} ')
                    with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                        arquivo_txt.write('Pesquisa sequencial base [Editora]: \n')
                        arquivo_txt.write(f"Editora: {id_registro}\nNome: {nome}\nPais: {pais}\nContato: {contato}\n{50*'='}\n")

                        print(f"Editora [{id_registro}] gravada no arquivo: '{self.caminho_txt}' com sucesso!")
                        print(f'Big0(pior caso): {math.ceil(num_registros)} | Execuções: {count}')
                        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')
                        print(f'{60 * "-"}')
                        return

            print('Pesquisa sequencial: Editora não encontrada!')
            with open(self.caminho_txt, 'a', encoding='utf-8') as arquivo_txt:
                arquivo_txt.write('Pesquisa sequencial: Editora não encontrada!')
    def embaralhar_base(self):
        if not os.path.exists(self.caminhocompleto):
            print(f'Base: "{self.caminhocompleto}" não encontrada para embaralhamento!')
            return

        tamanho_nome = 150
        tamanho_pais = 150
        tamanho_contato = 30
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
        print(f'Base: [editoras] embaralhada com sucesso!')
        os.remove(backup_file_path)
    def bubble_sort_base(self):
        temp_Inicial = time.time()
        if not os.path.exists(self.caminhocompleto):
            print(f'Base "{self.caminhocompleto}" não encontrada para ordenação!')
            return

        tamanho_nome = 150
        tamanho_pais = 150
        tamanho_contato = 30
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
        print(f'{60 * "-"}')
        print('Base: [editoras] ordenada com sucesso usando Bubble Sort.\n')
        print(f'Numero de comparações: {comparacoes}')
        print(f'Numero de trocas: {trocas}')
        print(f'Tempo decorrido na pesquisa: {(temp_Final - temp_Inicial)}s')

        return
