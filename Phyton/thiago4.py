print("Senha Fatorial")

minutos = int(input("Insira os minutos atuais do computador: "))

fat = minutos

for i in range (1,minutos):
    fat = fat*i

print("A senha é: LIBERDADE",fat)