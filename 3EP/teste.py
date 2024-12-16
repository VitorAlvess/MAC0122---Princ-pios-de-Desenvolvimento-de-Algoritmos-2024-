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


numeros = [45, 12, 89, 23, 56, 78, 34, 90, 67, 11]
