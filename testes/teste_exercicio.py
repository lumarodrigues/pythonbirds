from unittest import TestCase

from oo.exercicio import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)


# herdar da classe TestCase
# o nome do código e o método precisa ter o prefixo test