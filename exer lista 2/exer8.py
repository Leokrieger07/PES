divida = 1000  
juros_mensal = 15.30 / 100  + 1

meses = int(input("informe a quantidade de meses que deseja calcular: "))
cont = 0  

while cont < meses:
    divida *= juros_mensal 
    cont += 1  

print("Dívida total após", meses, "meses:", round(divida,2))
