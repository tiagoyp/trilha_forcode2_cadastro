pcsfuncionando = []
quebradois = [] # quebradois se refere ao total de pecas quebradas de todos os computadores
geradorid = 101  
def menu():
    cadastrando = False
    while True:
        cadastro = input("quer cadastrar um computador? digite s ou n: ").upper()  
        if cadastro in ("S", "N"):
            break
        else:
            print("por favor digite 's' ou 'n'.")
    if cadastro == "N":
        print("encerrando o cadastro. gostaria de ver as peças defeituosas, (digite 1) ver a lista de")
        escolha = input("computadores funcionando, (digite 2) ou ambos? (digite 3): ")
        if escolha != "1" and escolha != "2" and escolha != "3":
            print("por favor digite 1 ou 2")
            menu()
        elif escolha == "2" or escolha == "3":
            print(tuple(pcsfuncionando))
            cadastrando = False
        else:
            print(tuple(quebradois))
            cadastrando = False
        if escolha == "3":
            print(tuple(quebradois))
    elif cadastro == "S": 
        cadastrando = True
    return cadastrando
while menu():
    status = []
    quebradas = []
    status.append(geradorid)
    funf = input(f"computador de id {geradorid} funciona? (s/n)").upper()
    if funf == "S":
        funciona = True
        status.append(funciona)
        pcsfuncionando.append(geradorid)
        status.append(())
    elif funf == "N":
        funciona = False
        status.append(funciona)
    else:
        print("por favor digite s ou n")
    if funciona == False:
        quebradas = input(f"o computador de id {geradorid} tem quais peças quebradas? informe todas, separando-as com virgula e espaço: ")
        quebradois.append(tuple(quebradas.split(', ')))
        status.append(tuple(quebradas.split(', ')))
    geradorid += 1
    print(tuple(status))