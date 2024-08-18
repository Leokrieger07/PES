def par_ou_impar(n):
    return(n%2==0)

n=int(input("escreva um numero que deseja saber se é par ou impar: "))
    
if par_ou_impar(n):
    print(n, "é par")
else:
    print(n, "é impar")