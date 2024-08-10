class escrevetxt:
    def __init__(self, nomearq):
        self.nomearq = nomearq
        with open(nomearq,'w') as arquivo:
            arquivo.write(f'{20 * "="}BASE DE DADOS CRIADA{20 * "="}')

    def escrever(self, lista):
        with open(self.nomearq, 'a') as arquivo:
            for item in lista:
                if hasattr(item, 'toString'):
                    arquivo.write(item.toString() + '\n')
            arquivo.write('=' * 130 + '\n')
            print('já existe')

    
