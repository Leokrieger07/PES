c=[-1]*10

while True:
    print("menu")
    print("----")
    print("1.cadastrar")
    print("2.listar")
    print("0.sair")

    op=int(input("digite uma opção valida: "))

    if op==0:
        print("saindo...")
        break

    elif op==1:
        cod=int(input("escreva o codigo do produto: "))
        if cod == -1:
            print("Erro. Não é possível cadastrar um codigo -1.")
        elif cod in c:
            print("erro. codigo já cadastrado.")
        elif -1 in c:
            c[c.index(-1)]=cod
            print("codigo cadastrado com sucesso. ")
            
    
    if op ==2:
        for cod in c:
            if cod != -1:
                print(cod)
                

