import random
import time

lista =[]

Black = None
Read = None
Green = None

#moc
b = int(input('Podaj siłę zakręcenia --->' ))
a = random.randint(1,36)
c = b * a
moc = c // 2


user_input = input('Podaj liczbę od 1 do 38 lub napisz " C " aby wybrać kolor ---> ')

if user_input == 'C':
    user_input = input('||Black==1||Read==2||Green==3|| --->')

    if user_input == 1 or 2 or 3:

        if user_input == 1:
            Black = 1

        elif user_input == 2:
            Read = 2

        elif user_input == 3:
            Green = 3

for i in range(moc):
        time.sleep(0.25)
        r = random.randint(1,36)
        if r <10:
            print('[]','',r,'[]')
            print('########')
        
            lista.append(r)
        else:
            print('[]',r,'[]')
            print('########')

            lista.append(r)


if user_input == 1 or 2 or 3:
    if user_input and Black==1 and r==2 or r==4 or r== 6 or r==8 or r==10 or r==11 or r==13 or r==15 or r==17 or r==20 or r==22 or r==24 or r==26 or r==29 or r==28 or r==31 or r==33 or r==35:
        print('Zgadłeś kolor --->','Black')

    elif user_input== 2 and Read==2 and  r == 1  or r==3 or r==7 or r==9 or r==14 or r==16 or r==18 or r==19 or r==21 or r==23 or r==25 or r==27 or r==30 or r==32 or r==34 or r==36:
        print('Zgadłeś kolor ---> ','Read')

    elif user_input == 3 and Green == 3 and r == 0:
        print('Zgadłęś kolor --->','Green')

else:
    print('else color input')

if user_input == r:
    print('Wygrałeś')
    
elif user_input != r:
    print('Nie wygrałeś')


print('liczba to ---> ',r)
print('Twoja liczba to ---> ',user_input)
print('moc ---> ',moc)
print('Wszystkie liczby to ---> ',*lista)
