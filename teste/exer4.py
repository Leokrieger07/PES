
cadastro=[0]*15

while True:
    print("menu")
    print("----")
    print("1.cadastrar")
    print("2.listar")
    print("3.excluir")
    print("0.sair")

    op=int(input("Digite uma opção valida: "))
    if op == 0:
        print("saindo...")
        break

    elif op == 1:
        placa = input("escreva a sua placa: ")
        if placa == 0:
            print("placa invalida.")
        if placa in cadastro:
            print("placa já cadastrada: ")
        elif 0 in cadastro:
            cadastro[cadastro.index(0)]=placa 
    
    elif op == 2:
        for placa in cadastro:
            if placa !=0:
                print(placa)
    
    elif op == 3:
        rmv=input("ecreva a placa que deseja excluir: ")
        if placa in cadastro:
            cadastro.remove(rmv)
            print("placa removida com sucesso!")
        else:
            print("placa não encontrada.")
                

