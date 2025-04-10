import random
liczbacxykolor = input("Liczba czy kolor: ")
wylosowana =random.randint(1,36)
if liczbacxykolor == "kolor":
    if wylosowana == 36:
        print("Zielone")
    elif wylosowana % 2 == 0:
        print("Czerwone")
    elif wylosowana % 2 == 1:
        print("Czarnr")
elif licxbaczykolor == "liczba":
    liczbauser = int(input("Podaj liczbe: "))
    if liczbauser == wylosowana:
        print("Zgadłeś")
    else:
        print("Nie zgadłeś")

