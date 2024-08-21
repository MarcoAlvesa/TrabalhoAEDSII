import os


class EscreveArquivotxt:
    def __init__(self, ):

        os.makedirs("arquivos_txt", exist_ok=True)
        self.caminhocompleto = os.path.join("arquivos_txt", "Pesquisa.txt")

    def escreveItem(self, indice):
        if indice == -1:
            with open(self.caminhocompleto, 'a') as arquivo:
                arquivo.write(f'Objeto  não existe!\n')

        else:
            with open(self.caminhocompleto, 'a') as arquivo:
                arquivo.write(str('\n'))

    def escreveTexto(self, texto):
        with open(self.caminhocompleto, 'a') as arquivo:
            arquivo.write(texto)
