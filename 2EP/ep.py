import re

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    


class fracao:
    def __init__(self, numerador, denominador = 1):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()
    def __str__(self):
        return f"<{self.numerador} {self.denominador}>"
    def __add__(numero1, numero2):
        valor = fracao(numero1.numerador * numero2.denominador + numero2.numerador * numero1.denominador, numero1.denominador * numero2.denominador)
        valor.simplificar()
        return(valor)
    
    def simplificar(self):
        #Simplifica usando MDC
        def mdc(a, b):
            #MDC metodo de EUCLIDES (codigo curtinho)
            while b != 0:
                a, b = b, a % b
            return a

        mdc_valor = mdc(self.numerador, self.denominador)
        self.numerador //= mdc_valor  # Usa divisão inteira de mdc (opera com numeros não com fracao)
        self.denominador //= mdc_valor  # Usa divisão inteira de mdc (opera com numeros não com fracao)

        # Garante que o denominador seja positivo para não dar erro
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

        
    def __truediv__(self, outra):
        # Divisão de frações: multiplicamos pelo inverso da outra fração
        numerador = self.numerador * outra.denominador
        denominador = self.denominador * outra.numerador
        return fracao(numerador, denominador)
    
    def __mul__ (self,outra):
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        return fracao(numerador, denominador)
    
    def __sub__(self, outra):
        numerador = self.numerador * outra.denominador - self.denominador * outra.numerador
        denominador = self.denominador * outra.denominador
        return fracao(numerador, denominador)
    

def TraduzPosFixa(exp):
    pilha_operadores = Pilha()
    lista_exp_pos_fixa = []
    operadores = {'+': 1, '-': 1, '*': 2, '/': 2}
    unarios = {'+': 'unario+', '-': 'unario-'} #Operadores unarios para não dar erro com fração negativa

    tokens = re.findall(r"(\b\d*[\.]?\d+\b|[\(\)\+\*\-\/\%])", exp)

    for token in tokens:
        if token.isnumeric() or (token[0] == '-' and len(token) > 1 and token[1:].isnumeric()):
            # Token é um número ou número negativo (fazer dessa maneira se não da erro com o sinal de menos)
            lista_exp_pos_fixa.append(int(token))
        elif token in operadores:
            # Token é um operador
            while (not pilha_operadores.is_empty() and
                   pilha_operadores.peek() in operadores and
                   (operadores[token] <= operadores[pilha_operadores.peek()] or
                    (token in unarios and unarios[token] == 'unario-' and pilha_operadores.peek() == '**'))):
                lista_exp_pos_fixa.append(pilha_operadores.pop())
            pilha_operadores.push(token)
        elif token == '(':
            # Token é um parentese esquerdo
            pilha_operadores.push(token)
        elif token == ')':
            # Token é um parentese direito
            while (not pilha_operadores.is_empty() and pilha_operadores.peek() != '('):
                lista_exp_pos_fixa.append(pilha_operadores.pop())
            if not pilha_operadores.is_empty() and pilha_operadores.peek() == '(':
                pilha_operadores.pop()

    while not pilha_operadores.is_empty():
        lista_exp_pos_fixa.append(pilha_operadores.pop())

    print(lista_exp_pos_fixa)
    #A lista está em ordem porem não está transformando os numeros em fração. Codigo que faz isso está abaixo
    expressao = lista_exp_pos_fixa

    i = 0
    resultado = []
    
    while i < len(expressao):
        if i < len(expressao) - 2 and isinstance(expressao[i], int) and isinstance(expressao[i + 1], int) and expressao[i + 2] == '/':
            # Encontramos dois números seguidos por um "/"
            numerador = expressao[i]
            print("Numerador",numerador)
            denominador = expressao[i + 1]
            print("denominador",denominador)

            fracao_numero = fracao(numerador, denominador)  # Cria a fração
            resultado.append(fracao_numero)  # Adiciona a fração à lista de resultados
            i += 3  # Avança 3 posições
        else:
            # Caso contrário, simplesmente adiciona o elemento à lista de resultados
            resultado.append(expressao[i])
            i += 1
    return resultado

    return lista_exp_pos_fixa



def CalcPosFixa(listaexp):
    pilha_operandos = Pilha()
    for token in listaexp:
            if isinstance(token, fracao):
                # Token é um operando (número)
                pilha_operandos.push(token)
            else:
                if token == '+':
                    operand2 = pilha_operandos.pop()
                    operand1 = pilha_operandos.pop()
                    pilha_operandos.push(operand1 + operand2)
                if token == '-':
                    operand2 = pilha_operandos.pop()
                    operand1 = pilha_operandos.pop()
                    pilha_operandos.push(operand1 - operand2)
                if token == '*':
                    operand2 = pilha_operandos.pop()
                    operand1 = pilha_operandos.pop()
                    pilha_operandos.push(operand1 * operand2)
                if token == '/':
                    operand2 = pilha_operandos.pop()
                    operand1 = pilha_operandos.pop()
                    pilha_operandos.push(operand1 / operand2)


    if pilha_operandos.size() == 1:
        return pilha_operandos.pop()



if __name__== '__main__':
#   a = fracao(3,4)
#   b = fracao(1,2)
#   print(a-b)
    exp = "(2/3 + 5 / 2)* (3/5 - 5/3)"
    lista = TraduzPosFixa(exp)
    print(lista) # PERGUNTAR PARA O MONITOR SE ERA PARA PRINTAR ASSIM MESMO [<__main__.fracao object at 0x00000257DCE306D0>, <__main__.fracao object at 0x00000257DCE6A550>, '+', <__main__.fracao object at 0x00000257DCE6AD90>, <__main__.fracao object at 0x00000257DCE6A790>, '-', '*']
    print(lista[0] + lista[1])
    print(CalcPosFixa(lista))
EP 