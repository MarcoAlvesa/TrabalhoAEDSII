class Pesquisas:
    @staticmethod
    def pesquisa_binaria(lista, id):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio].id
            if chute == id:
                return meio
            if chute > id:
                alto = meio - 1
            else:
                baixo = meio + 1
        return -1

    @staticmethod
    def pesquisa_sequencial(lista, id):
        pos = 0
        found = False
        
        while pos < len(lista) and not found:
            if lista[pos].id == id:  # Comparando o id do objeto
                found = True
            else:
                pos = pos + 1

        return pos if found else None
