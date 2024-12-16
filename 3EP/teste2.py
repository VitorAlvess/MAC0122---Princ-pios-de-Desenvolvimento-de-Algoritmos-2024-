from datetime import datetime

# Lista original
data = [
    '34034310018,Felicia Ambulo Moncoes Casas,24/11/2014',
    '72236193023,Felicia Ambulo Moncoes Casas,04/04/2011',
    '34034310018,Felicia Ambulo Moncoes Casas,04/04/2011',
    '55169232241,Felicia Ambulo Moncoes Casas,16/10/2010',
    '34034310018,Felicia Ambulo Moncoes Casas,01/12/2001',
    '94062677273,Artmio Romulo Talento Lasmia,05/12/2007',
    '32652202769,Artmio Ambulo Sereno Casas,10/05/2003'
]

# Função para calcular a idade com base na data de nascimento
def calcula_idade(data_nascimento):
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# Função para extrair a chave de ordenação: nome, data de nascimento (convertida para datetime) e número
def chave_ordem(item):
    partes = item.split(',')
    numero = partes[0]  # Número de identificação (CPF)
    nome = partes[1]
    data_nascimento = partes[2]
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')  # Converte para datetime
    return (nome, nascimento, numero)  # Ordena por nome, data de nascimento e número


def heapify(lista, n, i): #Codigo do professor com modificações
    menor = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Filho esquerda maior q o nó
    if esquerda < n and lista[esquerda] < lista[menor]:
        menor = esquerda

    # filho direita maior q nó
    if direita < n and lista[direita] < lista[menor]:
        menor = direita

    # menor não for o nó atual trocas e chama recursivamente
    if menor != i:
        lista[i], lista[menor] = lista[menor], lista[i]
        heapify(lista, n, menor)


def heap_sort(arr): #codigo diferente do professor, o meu está ordenando de forma inversa. Achei mais facil assim
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)  # Reorganizar 

#lista de chaves para ordenação
chaves = [chave_ordem(item) for item in data]
print('Chaves', chaves)

# Ordenando com heap
heap_sort(chaves)

# Reconstruindo a lista ordenada com base nas chaves
ordenada = []
print(chaves)
for chave in chaves:
    for original_item in data:
        if chave_ordem(original_item) == chave:
            ordenada.append(original_item)
            break

# Exibindo a lista ordenada
print(ordenada.reverse())
for item in ordenada:
    print(item)
