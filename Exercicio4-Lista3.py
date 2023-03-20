timeA = str(input("Qual o nome do Time A: "))
numA = int(input("Quantos gols o Time A fez: "))

timeB = str(input("Qual o nome do Time A: "))
numB = int(input("Quantos gols o Time B fez: "))

if numA > numB:
    print("O ",timeA, " ganhou com ",numA, " gols do ", timeB, " com ",numB)
elif numA < numB:
    print("O ",timeB, " ganhou com ",numB, " gols do ", timeA, " com ",numA)
else:
    print("Empate")

