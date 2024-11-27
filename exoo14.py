#DESAFIO 14 A luguel de carro um programa que pergunte ao usuario a quantidade de km  percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugaudo . Calcule  o preço  a pagar sabendo que o carro custa r$60 por dia e r$ 0.15 por km

#Feito por Barbara Bastos no curso do Guanabara

k=float(input('====================== \n Ben-vindo(a) ao aplicativo da locatora de carros SONHO EM 4 RODAS! \n Por gentileza  digite os Km rodados :  '))
d=int(input(' Agora digite a quantidade de dias que o veiculo foi locado : '))
pd= d*60
pk= k* 0.15

print (f' ========================== \n O total da sua diaria em {d} dias foi de R$ {pd} \n Com o adicional de {k} Km rodado de {pk} \n  o total a pagar  será de R$ {pd+pk} ! \n ==================')