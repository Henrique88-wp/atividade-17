# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

a = int(input("Coloque qualquer ano"))
if a % 4==0 and a %100!=0 or a %400==0:
    print("O ano é bixesto")
else:
    print("O ano não é bixesto")