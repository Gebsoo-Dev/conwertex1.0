from modulkonwertera import *
print("Users guide: \n1 (potem zrobie")
wyborDzialania = int(input("Wybierz opcję: \n1 Sekundy na minuty\n2 Sekundy na godziny\n3 Minuty na sekundy\n4 Minuty na godziny\n5 Godziny na sekundy\n6 Godziny na minuty -> :"))

if (wyborDzialania == 1):
    sek = float(input("Podaj liczbę sekund: "))
    print(sekmin(sek))
    input("Wciśnij Enter aby wyjść")
elif (wyborDzialania == 2):
    sek = float(input("Podaj liczbę sekund: "))
    print (sekhour(sek))
    input("Wciśnij Enter aby wyjść")
elif (wyborDzialania == 3):
    min = float(input("Podaj liczbę minut: "))
    print(minsek(min))
    input("Wciśnij Enter aby wyjść")
elif (wyborDzialania == 4):
    min = float(input("Podaj liczbę minut: "))
    print(minhour(min))
    input("Wciśnij Enter aby wyjść")
elif (wyborDzialania == 5):
    hour = float(input("Podaj liczbę godzin: "))
    print(hoursek(hour))
    input("Wciśnij Enter by wyjść: ")
elif (wyborDzialania == 6):
    min = float(input("Podaj liczbę godzin: "))
    print(hourmin(min))
    print("Wciśnij Enter aby wyjść")
else:
    print("Niepoprawne dane wejścia")
    input("Wciśnij Enter aby wyjść")
  