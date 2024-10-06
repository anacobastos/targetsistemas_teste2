#Dado um vetor que guarda o valor de 
# faturamento diário de uma distribuidora, faça um programa, 
# na linguagem que desejar, que calcule e retorne:
#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

faturamento = [2000.00,3000.00,500.00,150.00,8950.00,0]
print("Considerando uma empresa com o faturamento de: ",faturamento)
min = 0
max = 0
cont = 1
dia_max = 1
dia_min = 1
qnt_dias = len(faturamento)
soma = 0
for valor in faturamento:
    soma = valor + soma    
    if max == 0: max = valor #setando o primeiro valor como maximo
    if min == 0: min = valor #setando o primeiro valor como maximo
    if valor>max: 
        max = valor
        dia_max = cont
    if valor<min: 
        min = valor
        dia_min = cont
    if(valor == 0):
        qnt_dias = qnt_dias - 1
    cont = cont+1 #pra saber qual dia 
media = soma/qnt_dias

print("O dia com maior rendimento foi o dia ",dia_max,", com rendimento de R$",max)
print("O dia com menor rendimento foi o dia ",dia_min,", com rendimento de R$",min)
cont = 0
for valor in faturamento:
    if valor>media:cont = cont+1

print("Tiveram ",cont," dias em que o faturamento foi maior que a media de R$",media)