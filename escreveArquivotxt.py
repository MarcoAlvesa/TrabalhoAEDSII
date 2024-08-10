class escreveArquivotxt:
    def __init__(self, nomearq):
        self.nomearq = nomearq
        with open(nomearq, 'w') as arquivo:
            arquivo.write(f'{22 * "="}-ARQUIVO CRIADO-{22 * "="}\n')

    def escreveLista(self, lista):
        with open(self.nomearq, 'a') as arquivo:
            for item in lista:
                # if hasattr(item, 'toString'):
                arquivo.write(item.__str__() + '\n')
            arquivo.write('=' * 60 + '\n')

    def escreveItem(self, lista, indice):
        if indice == -1:
            with open(self.nomearq, 'a') as arquivo:
                arquivo.write(f'Objeto  não existe!\n')
                arquivo.write('=' * 60 + '\n')
        else:
            with open(self.nomearq, 'a') as arquivo:
                arquivo.write(lista[indice].__str__() + '\n')
                arquivo.write('=' * 60 + '\n')

    def escreveTexto(self, texto):
        with open(self.nomearq, 'a') as arquivo:
            arquivo.write(texto)
