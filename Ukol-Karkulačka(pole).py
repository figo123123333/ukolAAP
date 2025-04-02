import random
cislo1 = int(input("zadejte první číslo "))
cislo2 = int(input("zadejte druhé číslo "))

vysledek = []
znamenko = input("zadejte +,-,*,/")

if znamenko == "+":
    soucet = cislo1+cislo2
    vysledek.append(soucet)
elif znamenko =="-":
    rozdil = cislo1-cislo2
    vysledek.append(rozdil)
elif znamenko == "*":
    soucin = cislo1*cislo2
    vysledek.append(soucin)
elif znamenko == "/":
    podil = cislo1/cislo2
    vysledek.append(podil)
else:
    print("špatné znaménko")

print(random.choice(vysledek))
print(vysledek)

opakovani = input ("chcete opakovat? ")

