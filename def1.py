#imposto
#aliquota - IR = 0.2 se o preco do produto for até 2000, acima disso a aliquota é 0.3
#aliquota - ISS = 0.15
#aliquota - CSLL = 0.05



def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2*preco
    else:
        imposto_ir = 0.3*preco
    imposto_iss = 0.15*preco
    imposto_csll = 0.05*preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

lista_preco=[]
qnt= int(input("escreva a quantidade de valores que deseja saber o imposto total: "))

for i in range (qnt):
    preco = float(input(f"escreva o {i+1}º valor: "))
    lista_preco.append(preco)
    
for preco in lista_preco:
    imposto_total = calcula_imposto_total(preco)
    print(f"imposto total sobre o produto de R${preco}: R${imposto_total}")
