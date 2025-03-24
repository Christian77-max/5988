import os
os.system("cls||clear")

opcao = int(input("""
código \t prato \t valor
1 \t Picanha \t\t R$ 250
2 \t lasanha \t\t R$ 20,00
3 \t strogonoff \t\t R$ 18,00
4 \t bife acebolado \t R$ 15,00
5 \t pão com ovo \t \t R$ 5,00

Digite a opção desejada:
 """))

while True:
    opcao = float(input("Escolher outro prato: "))
    
match opcao:
    case 1:
     refeicao = 25
    case 2:
        refeicao = 20
    case 3:
        refeicao = 18
    case 4:
        refeicao = 15
    case 5:
        refeicao = 5
    case _:
        print ("Errado")
comanda += refeicao


print("vou pegar a maquininha")
print("f"O total e: {comanda})