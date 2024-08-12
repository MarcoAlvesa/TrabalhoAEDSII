import os


class EscreverArquivobin:
    def __init__(self, nomearq):
        self.nomearq = nomearq
        os.makedirs("arquivos_bin", exist_ok=True)
        self.caminhocompleto = os.path.join("arquivos_bin", self.nomearq)
        with open(self.caminhocompleto, 'wb') as arquivo:
            arquivo.write(f'{22 * "="}-ARQUIVO CRIADO-{22 * "="}\n'.encode('utf-8'))

    def escreveLista(self, lista: list):
        with open(self.caminhocompleto, 'ab') as arquivo:
            for item in lista:
                arquivo.write((str(item) + '\n').encode('utf-8'))
            arquivo.write(('=' * 60 + '\n').encode('utf-8'))

    def escreveItem(self, lista: list, indice):
        if indice == -1:
            with open(self.caminhocompleto, 'ab') as arquivo:
                arquivo.write(f'Objeto  não existe!\n'.encode('utf-8'))
                arquivo.write(('=' * 60 + '\n').encode('utf-8'))
        else:
            with open(self.caminhocompleto, 'ab') as arquivo:
                arquivo.write((str(lista[indice]) + '\n').encode('utf-8'))
                arquivo.write(('=' * 60 + '\n').encode('utf-8'))

    def escreveTexto(self, texto):
        with open(self.caminhocompleto, 'ab') as arquivo:
            arquivo.write(texto.encode('utf-8'))
