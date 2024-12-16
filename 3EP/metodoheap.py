# versão recursiva
# aplica o Heap em a[k] na lista de n elementos
def Heap(a, k, n):
    # compara o filho esquerdo
    if 2*k <= n and a[k] < a[2*k]:
        # troca com o pai e aplica Heap ao novo filho
        a[k], a[2*k] = a[2*k], a[k]
        Heap(a, 2*k, n)
    # compara com o filho direito
    if 2*k+1 <= n and a[k] < a[2*k+1]:
        # troca com o pai e aplica Heap ao novo filho
        a[k], a[2*k+1] = a[2*k+1], a[k]
        Heap(a, 2*k+1, n)

def Heapsort(a):
    n = len(a) - 1 # a lista tem n + 1 elementos
    # aplica o Heap aos elementos acima da metade
    for k in range(n // 2, 0, -1):
        Heap(a, k, n)
    # a[1] é o maior. Troca com o último que já fica em seu lugar
    # aplica Heap em a[1] numa tabela com 1 elemento a menos
    while n >= 1:
        a[1], a[n] = a[n], a[1]
        Heap(a, 1, n - 1)
        n -= 1
numeros = [45, 12, 89, 23, 56, 78, 34, 90, 67, 11]
Heapsort(numeros)
print(numeros)
