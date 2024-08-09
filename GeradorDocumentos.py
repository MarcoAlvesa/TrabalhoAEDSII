import random

class GeradorDocumentos:
    def __init__(self):
        self.cnpj = self.generate_cnpj()

    def calculate_special_digit(self, lst):
        digit = sum(v * ((i % 8) + 2) for i, v in enumerate(lst))
        digit = 11 - digit % 11
        return digit if digit < 10 else 0

    def generate_cnpj(self):                                                       
        cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for _ in range(8)]             
        for _ in range(2):                                                          
            cnpj.insert(0, self.calculate_special_digit(cnpj))
        return '{}{}.{}{}{}.{}{}{}-{}{}'.format(*cnpj)

    def get_cnpj(self):
        return self.cnpj
