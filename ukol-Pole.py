skolniPomucky = ["sešit", "pero", "pravítko", "guma", "tužka", "fix"]

delkaPole = len(skolniPomucky)
print("Délka pole:", delkaPole)

print("Obsah pole:")
for pomucka in skolniPomucky:
    print(pomucka)

novaPomucka = input("galeidoskop ")
skolniPomucky.append(novaPomucka)

skolniPomucky.pop("fix")
print("Fix byl odstraněn")  

skolniPomucky.sort()

skolniPomucky.reverse()

print("Obrácené pořadí:")
for pomucka in skolniPomucky:
    print(pomucka)