passos = 0

def hanoi(n, origem, destino, auxiliar, nomes):
    if n == 1:
        destino.append(origem.pop())  # de origem para destino (topo)
        Mostre_Torres(*nomes)
    else:
        hanoi(n - 1, origem, auxiliar, destino, nomes)
        destino.append(origem.pop())  # de origem para destino (remanescente)
        Mostre_Torres(*nomes)
        hanoi(n - 1, auxiliar, destino, origem, nomes)

def Mostre_Torres(A, B, C):
    print(30 * ' -/-')
    print('')
    global passos 
    passos += 1
    print('Passo:', passos)
    altura = max(len(A), len(B), len(C))

    for i in range(altura, 0, -1): 
        # Imprime cada linha das torres, alinhando corretamente
        print(f"   {A[i-1] if i <= len(A) else ' '}        {B[i-1] if i <= len(B) else ' '}         {C[i-1] if i <= len(C) else ' '}")
    
    # Imprime a base das torres
    print(" TORRE A   TORRE B   TORRE C\n")

while True:
    try:
        discos = int(input('Digite uma quantidade válida de discos: '))
        if discos > 0:
            a = list(range(discos, 0, -1))
            b = []
            c = []
            # Nomes fixos das torres
            nomes = (a, b, c)
            Mostre_Torres(a, b, c)  # A = [3, 2, 1] B = [] C = []
            hanoi(discos, a, b, c, nomes)
            break
        else:
            print("Por favor digite um número maior que 0")
    except ValueError:
        print("Por favor digite um número inteiro válido")
