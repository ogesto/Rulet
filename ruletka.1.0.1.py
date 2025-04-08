#importowanie
import math
import random
import time
  

#kolory
Black = None
Red = None
Green = None
color = None
win = None


#listy
lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
listablack = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,]
listared = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
listagreen = [0]
loslista = []


#moc calculator
a = int(input('Podaj moc zakręcenia ---> '))
b = random.randrange(1,36)
c = a * b
d = c // 2
moc = d // 2


#user_imput = input('Podaj liczbę od 1 do 36 lub " C " aby wbrać kolor ')


#user imput number or color 
user_imput = input('Wpis "L" aby wybrać liczbę albo wpisz "C" aby wbrać kolor --->')



#color imput from user
if user_imput == "L" or "l" and user_imput != "C" or "c" :
        user_imput = int(input('Podaj liczbę od 0 d 36 --->'))
else:
    if user_imput == "C" or "c" and user_imput != "L" or "l":
        color = True
        user_imput = input('||Black==B||Red==R||Green==G|| --->')
        if user_imput == "B" or "b":
            Black = True
            color = True

        elif user_imput == "R" or "r":
            Red = True
            color = True

        elif user_imput == "G" or "g":
            Green = True
            color = True
    else:
        color = False
        print('color === False')

#losowanie liczb
for i in range(moc):
    
    los = random.randrange(0,36)
    time.sleep(0.25)
    if los <= 9:

        if los <10:
            print('[]','',los,'[]')
            print('########')
            loslista.append(los)

        elif los > 9:
            print('[]',los,'[]')
            print('########')
            loslista.append(los)

#number win chek
if user_imput in lista1:

    if user_imput == los:
        print('Wygrałeś')

    elif user_imput != los:
        print('Nie wygrałeś')

    
n = los % 2

#color win check

if color ==True:

    if Green == True and los == 0:
        print('You won --- Green')            
        win = True

    elif Red == True and n == 0:
        print('You won --- Red')
        win = True

    elif Black == True and n != 0:
        print('You won --- Black')
        win = True

#louse

if color == True and win != True:

    if los == 0:
        print('Color --- Green = you lost')            

    elif n == 0:
        print('Color --- Red = you lost')

    elif n != 0:
        print('Color --- Black = you lost')

if color == True or color != True and win != True:
    if los == 0:
        print('Color --- Green')            

    elif n == 0:
        print('Color --- Red')

    elif n != 0:
        print('Color --- Black')
