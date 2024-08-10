class escrevetxt:
    def __init__(self, nomearq, lista):
        self.nomearq = nomearq
        self.lista = lista

    def escrever(self):
        with open(self.nomearq, 'w') as file:
            for item in self.lista:
                if hasattr(item, 'tostring'):
                    file.write(item.tostring())
