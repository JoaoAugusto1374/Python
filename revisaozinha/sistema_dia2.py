pessoas = []

#pessoinha1 = {"nome": None, "idade": None}# cada pessoa é um dicionário, por isso não vale utilizar o mesmo saca.
#pessoinha2 = {"nome": None, "idade": None}

def adicionar_pessoa(lista, pessoa):
    lista.append(pessoa)
    

def listar(lista):
    return lista

#listar(pessoas)


def buscar_nome(lista, nome):
    for pessoa in lista:
        if pessoa["nome"] == nome:
            return pessoa 
    return None
    

def maiores_idade(lista):
    maiores = []
    for p in lista:
        if p["idade"] >= 18:
            maiores.append(p)
    
    return maiores
    

#maiores_idade(pessoas)


while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pelo nomme")
    print("4 - Mostrar maiores de idade")
    print("5 - Sair")

    try:
        op = int(input("Digite um número: "))
        if op == 1 or op == 2 or op == 3 or op == 4 or op == 5:
            if op == 5:
                break

            if op == 1:
                nome = input("Digite seu nome: ")
                try:
                    idade = int(input("Digite sua idade: "))
                except ValueError:
                    print("Idade inválida!")
                    continue 
                pessoa = {"nome": nome, "idade": idade}
                adicionar_pessoa(pessoas, pessoa)
            elif op == 2:
                listaPessoas = listar(pessoas)
                if len(listaPessoas) == 0:
                    print("Lista vazia!")
                else:
                    for p in listaPessoas:
                        print(p)
            elif op == 3:
                busca = input("Qual nome deseja buscar?: ")
                resultado = buscar_nome(pessoas, busca)
                if resultado is None:
                    print("Busca não encontrada")
                else:
                    print(resultado)
            elif op == 4:
                result = maiores_idade(pessoas)
                if len(result) == 0:
                    print("Nenhum encontrado!")
                else:
                    for v in result:
                        print(v)
        else:
            print("Digite uma opção no intervalo!")
    except ValueError:
        print("Digite uma opção válida")

    
    
