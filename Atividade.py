numero= input ("Digite um numero:")
numero= int (numero)
valida_positivo=numero>0
valida_negativo=numero>0
if valida_positivo:
    print("O numero é positivo")
elif valida_negativo:
    print("O numero é negativo")
else:
    print("O numero é zero")