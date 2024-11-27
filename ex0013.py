#Proximo desafio e fazer um programa que leia  o salario do funcionario e mostre seu novo salario com 15% de aumento

s=float(input('=================== \n Digite o valor do seu salario : R$ '))
ns= s + ( s * 15 / 100 )
print(f' Seu salario e de R$ {s:.2f}  \n com o aumento de 15% seu novo salario reajustado \n passa a ser de R$ {ns :.2f}')