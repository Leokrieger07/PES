inicio=int(input("escreva o numero que deseja que a tabuada comece: "))
fim=int(input("escreva o numero que deseja que a tabuada termine: "))
x=int(input("escreva o numero que deseja saber a tabuada: "))

if fim < inicio:
    print("invalido fim maior que inicio, escolha os numeros de inico e fim novamente")
    
while inicio<=fim:
    result=x*inicio
    print(x, "x", inicio, "=", result)
    inicio=inicio+1

    