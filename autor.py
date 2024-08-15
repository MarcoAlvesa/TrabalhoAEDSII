from faker import Faker
import struct
import os

class Autor:
    def __init__(self):
        self.id = None
        self.nome = ''
        self.datanasc = ''
        self.fake = Faker()

    def __str__(self):
        return f"Autor: [{self.id}] Nome: {self.nome}, Data de nascimento: {self.datanasc}"

    def gerador(self, tamanho):
        os.makedirs("Bases_dat", exist_ok=True)
        self.caminhocompleto = os.path.join("Bases_dat", "Autores.dat")
        with open(self.caminhocompleto, 'wb') as arquivo_binario:
            for i in range(tamanho):
                self.id = i + 1
                self.nome = self.fake.name()
                self.datanasc = self.fake.date_of_birth(minimum_age=20, maximum_age=90).strftime('%d/%m/%Y')
                autor = Autor

                idbinario = struct.pack('i', self.id)
                nome_binario = self.nome.encode('utf-8')
                datanasc_binario = self.datanasc.encode('utf-8')

                arquivo_binario.write(idbinario)
                arquivo_binario.write(nome_binario.ljust(50, b'\x00'))
                arquivo_binario.write(datanasc_binario.ljust(10, b'\x00'))
        print(f'Base de autores  gerado com sucesso! Tam----> [{tamanho}]')
