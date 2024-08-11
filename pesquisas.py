import math

class Pesquisas:
    @staticmethod
    def pesquisa_binaria(lista, id):
        baixo = 0
        alto = len(lista) - 1
        bigO = math.log(len(lista))
        count = 0
        while baixo <= alto:
            count += 1
            meio = (baixo + alto) // 2
            chute = lista[meio].id
            if chute == id:
                return meio, print(f"Execuções vs Big O: {count} vs O({bigO})")
            if chute > id:
                alto = meio - 1
            else:
                baixo = meio + 1
        return -1

    @staticmethod
    def pesquisa_sequencial(lista, id):
        pos = 0
        found = False
        bigO = len(lista)
        count = 0

        while pos < len(lista) and not found:
            count += 1
            if lista[pos].id == id:  # Comparando o id do objeto
                found = True
            else:
                pos = pos + 1

        return pos, print(f"Execuções vs Big O: {count} vs O({bigO})") if found else None
