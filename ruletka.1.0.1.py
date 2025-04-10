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
user_lista = []


#moc calculator
a = int(input('Enter the power of the spin ---> '))
b = random.randrange(1,36)
c = a * b
d = c // 2
moc = d // 2


#user_imput = input('Podaj liczbę od 1 do 36 lub " C " aby wbrać kolor ')


#user imput number or color 
user_imput = input('The entry "N" to select a number or enter "C" to enter a color --->')
user_lista.append(user_imput)


#color imput from user
if "N" in user_lista or "n" in user_lista:
        user_imput = int(input('Enter a number from 0 to 36 --->'))
        

if "C" in user_lista or "c" in user_lista:
    color = True
    user_imput = input('||Black==B||Red==R||Green==G|| --->')
    

    if user_imput == "B" or user_imput == "b":
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
        print('You won')

    elif user_imput != los:
        print("You didn't win")

    
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

if (color == True or color != True) and win != True:
    if los == 0:
        print('Color --- Green')            

    elif n == 0:
        print('Color --- Red')

    elif n != 0:
        print('Color --- Black')
