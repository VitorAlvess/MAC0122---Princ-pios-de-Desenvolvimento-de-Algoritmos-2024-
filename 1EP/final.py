
def hanoi(n,a,b,c, torrefixas): #Cologuei um argumento a mais 
  if n == 1:
    b.append(a.pop()) # de A para B (topo)
    Mostre_Torres(torrefixas[0],torrefixas[1],torrefixas[2])
  else:
    hanoi(n-1, a, c,b, torrefixas)
    b.append(a.pop()) # de A para B (o que sobrou)
    Mostre_Torres(torrefixas[0],torrefixas[1],torrefixas[2])
    hanoi(n-1,c,b,a, torrefixas)
def Mostre_Torres(A,B,C):
  altura = max(len(A), len(B), len(C)) #pegar a altura maxima 

  for i in range(altura, 0, -1): # [10, 0)
        print(f"   {A[i-1] if i <= len(A) else ' '}        {B[i-1] if i <= len(B) else ' '}         {C[i-1] if i <= len(C) else ' '}") #talvez essa não seja a melhor maneira de alinhar os textos

    # Imprime a base das torres
  print("TORRE A   TORRE B   TORRE C\n")








while True: # Looping Infinito igual o a saida sugerida 
    try:
        discos = int(input('Digite uma quantidade válida de discos: '))
        if discos > 0:
          a = list(range(discos, 0, -1))
          b = []
          c = []
          torrefixas = (a,b,c) # Criada para que os elementos das torres não se invertão.
          Mostre_Torres(torrefixas[0],torrefixas[1],torrefixas[2]) # A = [3, 2, 1] B = [] C = []
          hanoi(discos, a, b, c, torrefixas)
          
        else:
            print("Por favor digite um número maior que 0")
    except ValueError:
        print("Por favor digite um número inteiro válido")