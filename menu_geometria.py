print("Cálculo de Área")
print("Selecione a opção da figura geométrica:")
print("1) Retângulo")
print("2) Triângulo")
print("3) Círculo")
opcao = int(input("Informe: "))

if opcao == 1:
    base = float(input("Informe a base: "))
    altura = float(input("Informe a altura: "))

    area = base * altura
    print("A área do retângulo vale {}".format(area))

elif opcao == 2:
    base = float(input("Informe a base: "))
    altura = float(input("Informe a altura: "))

    area = base * altura / 2
    print("A área do triângulo vale {}".format(area))

elif opcao == 3:
    raio = float(input("Informe o raio: "))
    area = raio * raio * 3.1415
    print("A área do círculo é {}".format(area))
    
else:
    print("Nenhuma figura com a opção informada!")