nomes = ["joao", "maria", "ana", "paulinha"]
#duvida? Consigo deixar os nomes da própria lista em maiuculo? Ver isso na memória e tentar entender a resposta.
def nomes_maiusculo(lista):
    novaLista = []
    for n in lista:
        novaLista.append(n.upper())
    return novaLista


#a = nomes_maiusculo(nomes)
#print(a)

def nomes_mais_4letras(lista):
    novaLista = []
    for nome in lista:
        if len(nome) > 4:
            novaLista.append(nome)
    return novaLista

b = nomes_mais_4letras(nomes)
print(b)

def contar_nomes_a(lista):
    contador = 0
    for nome in lista: 
        if nome[0] == "a":
            contador += 1
    return contador

c = contar_nomes_a(nomes)
print(c)