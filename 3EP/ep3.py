from time import process_time
from datetime import datetime
class PilhaLista:

    '''Pilha como uma lista. (Codigo copiado da aula)'''

    def __init__(self):
        self._pilha = []
    def __len__ (self):
        return len(self._pilha)
    def is_empty(self):
        return len(self._pilha) == 0
    def push(self, e):
        self._pilha.append(e)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pilha vazia")
        return self._pilha.pop()


class Strings:

    """Classe que modifica como a string do programa deve ser comparada"""

    def __init__(self, strg):
        self.strg = strg
        self.strings = strg.split(',')
        self.nome = self.strings[1]
        self.data = self.strings[2].split('/')
        self.num = self.strings[0]

    def ComparaData(str1,str2):

        """Retorna True se a data da 1ª string é menor que a da 2ª"""

        dia1, dia2 = str1.data[0], str2.data[0]
        mes1, mes2 = str1.data[1], str2.data[1]
        ano1, ano2 = str1.data[2], str2.data[2]
        if ano1 == ano2:
            if mes1 == mes2:
                if dia1 < dia2: return True
                else: return False
            elif mes1 < mes2: return True
            else: return False
        elif ano1 < ano2: return True
        else: return False

    def __lt__(str1,str2):

        """Compara duas strings de acordo com as intruções,
           devolve True se a 1 for menor que a 2"""

        if str1.nome == str2.nome:
            if str1.data == str2.data:
                if str1.num == str2.num: return True
                elif str1.num < str2.num: return True
                else: return False
            elif str1.ComparaData(str2):return True
            else: return False
        elif str1.nome < str2.nome: return True
        else: return False

    def __str__(self):
        return self.strg

def chave_ordem(item):
        partes = item.split(',')
        numero = partes[0] 
        nome = partes[1]
        data_nascimento = partes[2]
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')  # Converte 
        return (nome, nascimento, numero)  

def ClassificaSort(TAB):
    # def calcula_idade(data_nascimento):
    #     nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    #     hoje = datetime.today()
    #     idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    #     return idade

   


    return sorted(TAB, key=chave_ordem)

def printBonito(TAB):
  for index,linha in enumerate(TAB, start=1):
    print(index,linha)
def comparacao(a,b,texto):
    if a == b: return print(f"*** {texto} - Classificação correta")
    return print("*** Classificação incorreta")
def Particiona(lista, inicio, fim):

    """Particiona mudando os elementos de lugar"""

    i, j = inicio, fim
    pivo = lista[fim]
    while True:
        # aumentando i
        while i < j and Strings(lista[i]) < Strings(pivo): i = i + 1
        if i < j: lista[i], lista[j] = pivo, lista[i]
        else: break
        # diminuindo j
        while i < j and Strings(pivo) < Strings(lista[j]): j = j - 1
        if i < j: lista[i], lista[j] = lista[j], pivo
        else: break
    return i
def ClassificaInserção_tim(TAB, esquerda, direita):


    for i in range(esquerda + 1, direita + 1):
        x = TAB[i]

        j = i -1
        while j >= esquerda and chave_de_ordenacao(x) < chave_de_ordenacao(TAB[j]):
            TAB[j + 1] = TAB[j]
            j -= 1

        TAB[j + 1] = x
def chave_de_ordenacao(elemento):
        #Ordem para o TIM
        partes = elemento.split(',')
        return (partes[1], datetime.strptime(partes[2], "%d/%m/%Y"), partes[0])

def ClassificaQuick(tab):

    # Método Quick Não Recursivo!!!!!!!!
    #Codigo do professor
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(tab) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    while not Pilha.is_empty():
        inicio, fim = Pilha.pop()
        # Só particiona se há mais de 1 elemento
        if fim - inicio > 0:
            k = Particiona(tab, inicio, fim)
            # Empilhe as sub-listas resultantes
            Pilha.push((inicio, k - 1))
            Pilha.push((k + 1, fim))
#copiado das aulas poucas modificacao nesse sort
def classificacaoMerge_tim(array, esquerda, m, r):
    array_tamanho1 = m - esquerda + 1
    array_tamanho2 = r - m
    direita_array = []
    esquerda_array = []
    #substitui o loop por esse modelo
    for i in range(0, array_tamanho1):
        esquerda_array.append(array[esquerda + i])

    for i in range(0, array_tamanho2):
        direita_array.append(array[m + 1 + i])

    i = 0
    j = 0
    k = esquerda

    while j < array_tamanho2 and i < array_tamanho1:
        if chave_de_ordenacao(esquerda_array[i]) <= chave_de_ordenacao(direita_array[j]):
            array[k] = esquerda_array[i]
            i += 1
        else:
            array[k] = direita_array[j]
            j += 1
        k += 1

    while i < array_tamanho1:
        array[k] = esquerda_array[i]
        i += 1
        k += 1

    while j < array_tamanho2:
        array[k] = direita_array[j]
        j += 1
        k += 1

def find_minrun(n):
    #Codigo do professor
    MINIMUM = 32
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r # é o tamanho do bloco

def ClassificaTIM(TAB):
    
    #Bem parecido com o do professor
    n = len(TAB)
    min_run = find_minrun(n)

    for i in range(0, n, min_run):
        ClassificaInserção_tim(TAB, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = left + size - 1
            right = min((left + size * 2 - 1), (n - 1))

            if mid < right:
                classificacaoMerge_tim(TAB, left, mid, right)

        size *= 2



def ClassificaHeap(lista): #Codigo do professor porem ordena o inverso
    n = len(lista)

    # Função auxiliar para garantir a ordem do heapyyyyyyy
    def heapify(lista, n, i):
        menor = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        # esquerda for menor que o nó 
        if esquerda < n and lista[esquerda] < lista[menor]:
            menor = esquerda

        # direita for menor que o nó 
        if direita < n and lista[direita] < lista[menor]:
            menor = direita

        # nó atual troca e chama recursivamente
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            heapify(lista, n, menor)

    # Construção do heap codigo do professor  mas alterado 
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Ordenando a lista, retirando o maior valor (raiz do heap) repetidamente
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Troca o maior com o último elemento
        heapify(lista, i, 0)  # Reorganiza o heap 
    ordenada = []
    
    for chave in lista:
        for original_item in linhas4:
            if chave_ordem(original_item) == chave:
                ordenada.append(original_item)
                break
    ordenada.reverse()
    return ordenada  # Retorna a lista já ordenada




if __name__ == '__main__':
    arquivo = input('Digite o nome do arquivo:')
   
    while arquivo != "fim":

        with open(arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        linhas = conteudo.strip().split('\n') #Strip antes para cuidar das imperfeições
        linhas2 = linhas[:]
        linhas3 = linhas[:]
        linhas4 = linhas[:]


        t = process_time()
        final = ClassificaSort(linhas)
        print('Tempo de classificação sort() = {}'.format(process_time() - t))
      
        
        
        chaves = [chave_ordem(item) for item in linhas4]
        t = process_time()
        ordenada = ClassificaHeap(chaves)
        print('Tempo de classificação HEAP() = {}'.format(process_time() - t))
        comparacao(ordenada,final,'Heap')



        t = process_time()
        ClassificaQuick(linhas2)
        print('Tempo de classificação Quick() = {}'.format(process_time() - t))
        comparacao(linhas2,final,'Quick')
        
        t = process_time()
        ClassificaTIM(linhas3)
        print('Tempo de classificação TIM() = {}'.format(process_time() - t))
        comparacao(linhas3,final,'TIM')

       
        
        
       

            

        arquivo = input('Digite o nome do arquivo:')