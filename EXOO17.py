#desafio de sortear os alunos
# barabara bastos


import random



#importando nosso modulo que vai fazer o sorteio o randon

n1=input('primeiro aluno : ')
n2=input('segundo aluno : ')
n3=input('terceiro aluno : ')
n4=input('quarto aluno : ')
lista= [n1 , n2, n3, n4]
e=random.choice(lista)
print (f'o aluno escolhido foi {e}')


