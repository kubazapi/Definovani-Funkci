import math

def scitani(vysledek, cislo2):
     return vysledek + cislo2

def odcitani(vysledek, cislo2):
    return vysledek - cislo2

def nasobeni(vysledek, cislo2):
    return vysledek * cislo2

def deleni(vysledek, cislo2):
        return vysledek / cislo2

def mocnina(vysledek, cislo2):
    return vysledek ** cislo2

def odmocnina(vysledek, cislo2):
    return vysledek

def pocitani(operace, vysledek, cislo2):
    if operace == "+":
        return scitani(vysledek, cislo2)
    elif operace == "-":
        return odcitani(vysledek, cislo2)
    elif operace == "*":
        return nasobeni(vysledek, cislo2)
    elif operace == "/":
        return deleni(vysledek, cislo2)
    elif operace == "**":
        return mocnina(vysledek, cislo2)
    elif operace == "//":
        return odmocnina(vysledek)
    else:
        print("Tahla operace není podporována.")
        return None

def kalkulacka():
  print("Vítej v kalkulaèce")
while True:
  cislo1 = float(input("Zadej èíslo: "))
  cislo2 = float(input("Zadej èíslo: "))
  operace = input("Zadej operaci: ")
  if operace == "+":
    print(cislo1 + cislo2)
  elif operace == "-":
    print(cislo1 - cislo2)
  elif operace == "*":
    print(cislo1 * cislo2)
  elif cislo2 == 0 and operace == "/":
    print("Nulou nelze dìlit")
  elif operace == "/":
    print(cislo1 / cislo2)
  elif operace == "**":
    print(cislo1 ** cislo2)
  elif operace == "//":
    print(cislo1 // cislo2)
  else:
    print("Zadaná hodnota je nesprávná")
  pokracovat = input("Chceš pokraèovat? (ano/ne): ")
  if pokracovat == "ne":
    print("Dìkuji za použití kalkulaèky")
    break
