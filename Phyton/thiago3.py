print("Médias das turmas")

mediaimpar = 0
mediapar = 0

for i in range (1,51, 2):
        print("VOCÊ DEVE INSERIR OS ALUNOS DA TURMA IMPAR")
        notaimpar = int(input("Insira a nota do aluno " + str(i) + ": "))
        mediaimpar = mediaimpar + notaimpar

for i in range (2,51,2):    
        print("VOCÊ DEVE INSERIR OS ALUNOS DA TURMA PAR")
        notapar = int(input("Insira a nota do aluno " + str(i) + ": "))
        mediapar = mediapar + notapar

totimpar = mediaimpar/25
totpar = mediapar/25

print("A média total da turma ímpar foi: ", totimpar)
print("A média total da turma par foi: ", totpar)

if totpar > totimpar:
    print("A turma par teve maior média")
else:
    print("A turma ímpar teve a maior média")