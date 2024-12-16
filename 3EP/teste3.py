from datetime import datetime

# Lista de exemplo
data = [
    '34034310018,Felicia Ambulo Moncoes Casas,24/11/2014',
    '72236193023,Felicia Ambulo Moncoes Casas,04/04/2011',
    '34034310018,Felicia Ambulo Moncoes Casas,04/04/2011',
    '55169232241,Felicia Ambulo Moncoes Casas,16/10/2010',
    '34034310018,Felicia Ambulo Moncoes Casas,01/12/2001',
    '94062677273,Artmio Romulo Talento Lasmia,05/12/2007',
    '32652202769,Artmio Ambulo Sereno Casas,10/05/2003'
]
arquivo = 'nomes.txt'
   

with open(arquivo, 'r') as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.strip().split('\n') #Strip antes para cuidar das imperfeições
linhas2 = linhas[:]
linhas3 = linhas[:]
linhas4 = linhas[:]


# Função para calcular a idade com base na data de nascimento
def calcula_idade(data_nascimento):
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# Função para gerar a chave de ordenação
def chave_ordem(item):
    partes = item.split(',')
    numero = partes[0]  # Número de identificação (CPF)
    nome = partes[1]
    data_nascimento = partes[2]
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')  # Converte para datetime
    return (nome, nascimento, numero)  # Ordena por nome, data de nascimento e número

# Função para construir o heap, ordenar e retornar a lista ordenada
def heap_sort(lista):
    n = len(lista)

    # Função auxiliar para garantir a ordem do heap
    def heapify(lista, n, i):
        menor = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        # Se o filho da esquerda for menor que o nó atual
        if esquerda < n and lista[esquerda] < lista[menor]:
            menor = esquerda

        # Se o filho da direita for menor que o nó atual
        if direita < n and lista[direita] < lista[menor]:
            menor = direita

        # Se o menor não for o nó atual, trocamos e chamamos recursivamente
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            heapify(lista, n, menor)

    # Construção do heap (reorganiza a lista para um heap válido)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Ordenando a lista, retirando o maior valor (raiz do heap) repetidamente
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Troca o maior (root) com o último elemento
        heapify(lista, i, 0)  # Reorganiza o heap com o tamanho reduzido
    ordenada = []
    for chave in lista:
        for original_item in linhas4:
            if chave_ordem(original_item) == chave:
                ordenada.append(original_item)
                break
    ordenada.reverse()
    return ordenada  # Retorna a lista já ordenada

# Criando a lista de chaves para ordenação
chaves = [chave_ordem(item) for item in linhas4]

# Ordenando com heap sort e retornando a lista ordenada
ordenada = heap_sort(chaves)

# Exibindo a lista ordenada

print(ordenada)

