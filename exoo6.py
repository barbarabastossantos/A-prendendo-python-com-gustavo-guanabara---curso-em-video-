import math

#DESAFIO 06 fazer o calculo do dobro, triplo e raiz de um numero que o usuario escolher . Para a raiz fiz a import da biblioteca math

n= (int(input('==========================================================\n Ola! Tudo bem? Vamos começar com nossos calculos! \n  Preparado(a)? Então vamos lá ! \n Digite um número : ')))
print(f' O número que você escolheu foi {n} .\n O dobro de {n} é {n*2} .\n O triplo de {n} é {n*3} . \n  A raiz quadrada de {n} é  {math.sqrt(n):.2f}')