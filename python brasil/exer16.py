
#feito pelo chat  

# Inicializando a lista de contadores para armazenar o número de vendedores em cada faixa salarial
faixas_salariais = [0] * 10  # 10 faixas salariais

# Solicitando ao usuário que insira as vendas brutas de cada vendedor
num_vendedores = int(input("Quantos vendedores você deseja analisar? "))
for i in range(num_vendedores):
    vendas_brutas = float(input(f"Insira as vendas brutas do vendedor {i+1}: "))
    
    # Calculando o salário do vendedor
    salario = 200 + 0.09 * vendas_brutas
    
    # Determinando a posição na lista com base no salário
    posicao = int(salario // 100)  # Divide o salário por 100 e arredonda para baixo para obter a posição
    
    # Incrementando o contador na posição correspondente na lista
    if posicao < 9:
        faixas_salariais[posicao] += 1
    else:
        faixas_salariais[9] += 1

# Mostrando o número de vendedores em cada faixa salarial
print("Número de vendedores em cada faixa salarial:")
for i in range(9):
    print(f"${200 + i*100} - ${299 + i*100}: {faixas_salariais[i]}")
print("$1000 em diante: ", faixas_salariais[9])
