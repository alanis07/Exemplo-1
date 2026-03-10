nota=input("Digite a nota do Aluno(a)")
nota=float(nota)
notalta=nota>=6.0
notabaixa=nota<6.0

if notalta:
    print(f"A nota do aluno:{nota} aluno aprovado")

else:
    print(f"A nota do aluno: {nota} aluno reprovado")