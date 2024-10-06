#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

frases = ["palavra","capivara","processo","internet das coisas"]

for frase in frases:
    inverso = ""
    tam = len(frase)
    for i in range(0,tam):
        letra = frase[tam-i-1]
        inverso = inverso + letra
    print(frase, "->", inverso)