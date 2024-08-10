class Pesquisas:
    def pesquisa_binaria(self, lista, item):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]
            if chute.id == item:
                return meio
            if chute.id > item:
                alto = meio - 1
            else:
                baixo = meio + 1
        return None
 
    def pesquisa_sequencial(self, lista, item):
        pos = 0
        found = False
        
        while pos < len(lista) and not found:
            if lista[pos].id == item:  # Comparando o id do objeto
                found = True
            else:
                pos = pos + 1

        return pos if found else None