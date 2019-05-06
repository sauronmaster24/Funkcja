
############################
import random
import time
from colorama import init
from termcolor import colored
init()
#############################

def potega_lub_pierwiastek(x):
    if x%2 == 0:
        return x**2
    else:
        return round(x ** 0.5,2)






liczba = int(input("Podaj liczbę, błagam Cię:  "))
wynik = potega_lub_pierwiastek(liczba)
print(wynik)
