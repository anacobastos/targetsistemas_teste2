# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual
# de representação que cada estado teve dentro do valor total mensal da distribuidora.  
faturamento_estados = ['SP','RJ','MG','ES','OUTROS']
faturamento_valores = [67836.43,36678.66,29229.88, 27165.48,19849.53]

#encontrando o faturamento mensal total
total = 0
for valor in faturamento_valores:
    total = total + valor

#Verificando a porcentagem de cada local
i = 0
faturamento_porc = list()
for valor in faturamento_valores:
    faturamento_porc.append(round(valor/total*100, 2))
    
#imprimindo o resultado
i = 0
for estado in faturamento_estados:
    print(estado,"representou ",faturamento_porc[i]," % do faturamento mensal da empresa")
    i = i+1