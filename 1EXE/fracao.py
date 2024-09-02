class Fracao:
    def __init__(self, numerador = 0, denominador = 1):
        self.cima = numerador
        self.baixo = denominador
    def __mul__(p1, p2):
        mult_cima = p1.cima * p2.cima
        mult_baixo = p1.baixo * p2.baixo
        return Fracao(mult_cima, mult_baixo)

    def __str__(d):
        return "/" + str(d.cima) + " " + str(d.baixo) + "/"
    
    def __add__(p1, p2):
        soma_cima = p1.cima * p2.baixo + p2.cima * p1.baixo
        soma_baixo = p1.baixo * p2.baixo
        return Fracao(soma_cima, soma_baixo)
