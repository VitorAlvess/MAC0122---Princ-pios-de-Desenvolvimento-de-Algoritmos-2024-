class Duplas:

    '''Define a classe Duplas.'''
    # Construtor da classe
    def __init__(self, p1 = 0, p2 = 0):
        '''Construtor da classe.'''
        self.primeiro = p1
        self.segundo = p2
        # Retorna a soma de dois elementos da classe
    def __add__(d1, d2):
        pri = d1.primeiro + d2.primeiro
        seg = d1.segundo + d2.segundo
        return Duplas(pri, seg)
    # Transforma uma Dupla em string para imprimir no formato / a b /
    def __str__(d):
        return "/" + str(d.primeiro) + " " + str(d.segundo) + "/"
# Exemplos de uso da classe
# /3 4/
