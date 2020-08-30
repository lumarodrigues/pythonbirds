'''
Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> Dir = Direcao()
    >>> Dir.direcao
    'Norte'
    >>> Dir.girar_a_direita()
    >>> Dir.direcao
    'Leste'
    >>> Dir.girar_a_direita()
    >>> Dir.direcao
    'Sul'
    >>> Dir.girar_a_direita()
    >>> Dir.direcao
    'Oeste'
    >>> Dir.girar_a_direita()
    >>> Dir.direcao
    'Norte'
    >>> Dir.girar_a_esquerda()
    >>> Dir.direcao
    'Oeste'
    >>> Dir.girar_a_esquerda()
    >>> Dir.direcao
    'Sul'
    >>> Dir.girar_a_esquerda()
    >>> Dir.direcao
    'Leste'
    >>> Dir.girar_a_esquerda()
    >>> Dir.direcao
    'Norte'
    >>> carro = Carro(motor, Dir)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

'''

class Carro:

    def __init__(self, motor, Dir):
        self.Dir = Dir
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.Dir.direcao

    def girar_a_direita(self):
        self.Dir.girar_a_direita()

    def girar_a_esquerda(self):
        self.Dir.girar_a_esquerda()

class Motor:

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0
        return self.velocidade

class Direcao:
    direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
    contador = 0

    def __init__(self, direcao = 'Norte'):
        self.direcao = direcao

    def girar_a_direita(self):
        self.contador += 1
        if self.contador > 3:
            self.contador = 0
        self.direcao = self.direcoes[self.contador]
        return self.direcoes[self.contador]

    def girar_a_esquerda(self):
        self.contador -= 1
        if self.contador < 0:
            self.contador = 3
        self.direcao = self.direcoes[self.contador]
        return self.direcoes[self.contador]


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    print(motor.acelerar())
    print(motor.acelerar())
    print(motor.acelerar())
    print(motor.frear())
    print(motor.frear())

    Dir = Direcao()
    print(Dir.direcao)
    print(Dir.girar_a_direita())
    print(Dir.girar_a_direita())
    print(Dir.girar_a_direita())
    print(Dir.girar_a_direita())
    print(Dir.girar_a_esquerda())
    print(Dir.girar_a_esquerda())
    print(Dir.girar_a_esquerda())
    print(Dir.girar_a_esquerda())
'''
Rodar doctest via linha de comando: python -m doctest exercicio.py
'''
