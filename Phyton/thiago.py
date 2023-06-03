print("VOTAÇÃO DA LIVE")

seg = int(input("Insira a quantidade de votos de Segunda-Feira: "))
ter = int(input("Insira a quantidade de votos de Terça-Feira: "))
qua = int(input("Insira a quantidade de votos de Quarta-Feira: "))
qui = int(input("Insira a quantidade de votos de Quinta-Feira: "))
sex = int(input("Insira a quantidade de votos de Sexta-Feira: "))

vencedor = "Segunda-Feira"

if ter > seg:
    vencedor = "Terça-Feira"
    if qua > ter: 
        vencedor = "Quarta-Feira"
        if qui > qua: 
            vencedor = "Quinta-Feira"
            if sex > qui: 
                vencedor = "Sexta-Feira"

print("O dia vencedor foi", vencedor)