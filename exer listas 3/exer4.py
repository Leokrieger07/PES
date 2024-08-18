cadastro=[0]*15

while True:

    #menu
    print("menu:")
    print("--------")
    print("1. cadastrar")
    print("2.excluir")
    print("3. listar")
    print("0. sair")

    #escolha um opção 
    opcao=int(input("escolha um opcao: "))

    #opção 1: cadastrar uma nova placa 
    if opcao==1:
        placa=(input("escreva a placa do veículo"))
        if placa in cadastro:
            print("placa já cadastrada")
        elif 0 in cadastro:
            cadastro[cadastro.index(0)]=placa 
            print("placa cadastrada com sucesso!")
        else:
            print("limite de placas cadastradas alcansado")
    
    #opção 2:excluir uma placa
    elif opcao == 2:
        remover=(input("escreva a placa que deseja remover"))
        if remover in cadastro:
            cadastro.remove(remover)
            print("placa removida com sucesso!")
        else:
            print("a placa não foi encontrada")

    #opção 3: listar as placas cadastradas
    elif opcao == 3:
        for placa in cadastro:
            if placa!=0:
                print(placa)
              
    #opção 0: sair 
    elif opcao ==0:
        print("saindo...")
        break

            

