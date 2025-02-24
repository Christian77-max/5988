import os
os.system("clear")

primeiro_numero = float(input("digite o primeiro numero"))
segundo_numero = float(input("digite o segundo numero"))

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = primeiro_numero
    maior = segundo_numero

print("maior:", (maior))
print("segundo:", (menor))