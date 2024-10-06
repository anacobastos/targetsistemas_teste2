n = int(input("Escolha um numero: "))
print(n,"pertence a fibonacci?")
if(n<0):
    print("Escolha um numero valido")
else:
    atual = 1
    ant = 0
    for i in range(1,n):
        fib = atual + ant
        print(atual,"+",ant,"=",fib)
        if(fib==n): 
            print("Sim! ",n,"pertence a sequencia de fibonacci")
            break
        if(fib>n):        
            print(n, "não pertence a sequencia de fibonacci")
            break
        ant = atual
        atual = fib
    
 