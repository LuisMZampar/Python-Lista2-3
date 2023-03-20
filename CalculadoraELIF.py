#resolver uma conta: 34.6 * 4.8 = 166.08

numA = float(input("Informe o 1º número: "))
op = input("Operação (+-*/): ")
numB = float(input("Informe o 2º número: "))

resultado = 0
fez_conta = True

if op == '+':
    resultado = numA + numB
elif op == '-':
    resultado = numA - numB
elif op == '*':
    resultado = numA * numB
elif op == '/':
    resultado = numA / numB
else:
    print("Operador informado inválido!")
    fez_conta = False
    #devo encerrar o algoritmo aqui, logo depois do print
    #exit()

if fez_conta == True:
    print("O resultado da expressao é", resultado)                