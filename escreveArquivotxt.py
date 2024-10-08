import os


class EscreveArquivotxt:
    def __init__(self, nomearq):
        self.nomearq = nomearq
        os.makedirs("arquivos_txt", exist_ok=True)
        self.caminhocompleto = os.path.join("arquivos_txt", self.nomearq)
        with open(self.caminhocompleto, 'w') as arquivo:
            arquivo.write(f'{22 * "="}-ARQUIVO CRIADO-{22 * "="}\n\n')

    def escreveLista(self, lista):
        with open(self.caminhocompleto, 'a') as arquivo:
            for item in lista:
                # if hasattr(item, 'toString'):
                arquivo.write(str(item) + '\n')
            arquivo.write('=' * 60 + '\n')

    def escreveItem(self, lista, indice):
        if indice == -1:
            with open(self.caminhocompleto, 'a') as arquivo:
                arquivo.write(f'Objeto  não existe!\n')

        else:
            with open(self.caminhocompleto, 'a') as arquivo:
                arquivo.write(str(lista[indice]) + '\n')


    def escreveTexto(self, texto):
        with open(self.caminhocompleto, 'a') as arquivo:
            arquivo.write(texto)
