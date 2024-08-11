import math

class Merge:
    def __init__(self, lista, key=lambda x: x):
        self.lista = lista
        self.key = key
        self.count = 0
        self.bigO = len(lista) * math.log(len(lista))

    def merge_sort(self, lista):
        if len(lista) > 1:
            self.count += 1
            # pegando o meio da lista;
            mid = len(lista) // 2
            #Primeira e segunda metade da lista;
            plado = lista[:mid]
            slado = lista[mid:]

            self.merge_sort(plado)
            self.merge_sort(slado)

            i = j = k = 0

            while i < len(plado) and j < len(slado):
                self.count += 1
                if self.key(plado[i]) < self.key(slado[j]):
                    lista[k] = plado[i]
                    i += 1
                else:
                    lista[k] = slado[j]
                    j += 1
                k += 1

            # Verificar se há elementos restantes no p_lado
            while i < len(plado):
                self.count += 1
                lista[k] = plado[i]
                i += 1
                k += 1

            # Verificar se há elementos restantes no s_lado
            while j < len(slado):
                self.count += 1
                lista[k] = slado[j]
                j += 1
                k += 1

    def sort(self):
        self.merge_sort(self.lista)
        print(f"Execuções vs Big O: {self.count} vs O({self.bigO})")
    