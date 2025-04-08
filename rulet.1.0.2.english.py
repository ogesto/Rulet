import random
import time

# Kolory
Black = False
Red = False
Green = False
color = False
win = False

# Listy
lista1 = list(range(37))
listablack = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
listared = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
listagreen = [0]

# Użytkownik podaje moc zakręcenia
a = int(input('Enter the power of the spin ---> '))
b = random.randint(1, 36)
c = a * b
d = c // 2
moc = d // 2

# Wybór użytkownika: liczba lub kolor
user_input = input('Enter "N" for number or "C" for color ---> ').strip().upper()

if user_input == "N":
    try:
        user_input = int(input('Enter a number from 0 to 36 ---> '))
    except ValueError:
        print("Invalid number!")
        exit()
elif user_input == "C":
    color = True
    user_input = input('|| Black=B || Red=R || Green=G || ---> ').strip().upper()

    if user_input == "B":
        Black = True
    elif user_input == "R":
        Red = True
    elif user_input == "G":
        Green = True
    else:
        print("Invalid color!")
        exit()
else:
    print("Invalid choice!")
    exit()

# Losowanie liczby
los = random.randint(0, 36)
print(f"Winning number: {los}")

# Sprawdzanie wygranej dla liczby
if isinstance(user_input, int):
    if user_input == los:
        print('You won!')
    else:
        print("You didn't win.")

# Sprawdzanie wygranej dla koloru
else:
    n = los % 2
    if Green and los == 0:
        print('You won --- Green')
        win = True
    elif Red and n == 0:
        print('You won --- Red')
        win = True
    elif Black and n != 0:
        print('You won --- Black')
        win = True

# Przegrana
if not win:
    print("You lost!")
