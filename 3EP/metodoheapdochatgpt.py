def Heap(a, k, n):
    """
    Função recursiva que aplica o heap no índice `k` da lista `a` de tamanho `n`.
    """
    maior = k
    esquerda = 2 * k
    direita = 2 * k + 1

    # Se o filho da esquerda for maior que o pai, troca os elementos
    if esquerda <= n and a[esquerda - 1] > a[maior - 1]:
        maior = esquerda

    # Se o filho da direita for maior que o pai ou o filho esquerdo, troca os elementos
    if direita <= n and a[direita - 1] > a[maior - 1]:
        maior = direita

    # Se o maior não é o pai, troque e aplique o heap no nó trocado
    if maior != k:
        a[k - 1], a[maior - 1] = a[maior - 1], a[k - 1]  # Troca
        Heap(a, maior, n)  # Recursão para aplicar o heap nos filhos

def Heapsort(a):
    """
    Função que ordena a lista `a` utilizando o algoritmo Heap Sort.
    """
    n = len(a)  # Tamanho da lista

    # Passo 1: Construir o heap a partir dos elementos (do meio para o início)
    for k in range(n // 2, 0, -1):
        Heap(a, k, n)

    # Passo 2: Ordenar trocando o maior (raiz) com o último elemento e refazendo o heap
    while n > 1:
        a[0], a[n - 1] = a[n - 1], a[0]  # Troca o maior elemento com o último
        n -= 1  # Reduz o tamanho da heap
        Heap(a, 1, n)  # Refaz o heap a partir da raiz (índice 1)

# Exemplo de uso:
numeros = [45, 12, 89, 23, 56, 78, 34, 90, 67, 11]
Heapsort(numeros)
print(numeros)
