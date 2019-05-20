class Pessoa:
    def __init__(self, idade, altura, peso, sexo):
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo

    def imprimir(self):
        print('pessoa1.idade', pessoa1.idade)
        print('pessoa1.altura', pessoa1.altura)
        print('pessoa1.peso', pessoa1.peso)
        print('pessoa1.sexo', pessoa1.sexo)


class PessoaAlternativa:
    def __init__(self):
        self.idade = None
        self.altura = None
        self.peso = None
        self.sexo = None


if __name__ == '__main__':
    pessoa1 = Pessoa(20, 150, 50, 'M')
    pessoa1.imprimir()

    pessoa2 = PessoaAlternativa()
    pessoa2.idade = 20
    pessoa2.altura = 160
    pessoa2.peso = 70
    pessoa2.sexo = 'F'

    print('pessoa2.idade', pessoa2.idade)
    print('pessoa2.altura', pessoa2.altura)
    print('pessoa2.peso', pessoa2.peso)
    print('pessoa2.sexo', pessoa2.sexo)
