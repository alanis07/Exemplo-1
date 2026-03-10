nota=input("Digite a nota do Aluno(a)")
nota=float(nota)
notalta=nota>=6.0
notabaixa=nota<6.0

if notalta:
    print("Anota do aluno:{nota} aluno aprovado")

else:
    print("A nota do aluno: {nota} aluno reprovdo")