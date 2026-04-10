
lista = []

def adicionar_num(lista, n):
    lista.append(n)
    
def lista_numeros(lista):
    if len(lista) == 0:
        print("lista vazia!")
    else:
        for v in lista:
            print(v)

def maior_num(lista):
    if len(lista) == 0:
        print("Lista vazia")
    
    mai = lista[0]
    for v in lista:
        if v > mai:
            mai = v 
    return mai

def menor_num(lista):
    if len(lista) == 0:
        print("Lista vazia")
    
    menor = lista[0]
    for v in lista:
        if v < menor:
            menor = v 
    return menor

while True:
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Mostrar maior número")
    print("4 - Mostrar menor número")
    print("5 - Sair")
    
    try:
        op = int(input("Digite a sua opção: "))
    except ValueError:
        print("Digite um número válido")
        continue
    
    if op == 5:
        break 
    else:
        if op == 1:
            numero = int(input("Digite o número que deseja adicionar: "))
            adicionar_num(lista, numero)
        elif op == 2:
            lista_numeros(lista)
        elif op == 3:
            maior = maior_num(lista)
            print(maior)
        elif op == 4:
            men = menor_num(lista)
            print(men)
            
