# Einfache Mathematik
a = 7
b = 5

print("Addition: ", a + b)
print("Subtraktion: ", a - b)
print("Multiplikation: ", a * b)
print("Division: ", a / b)

# Durchschnitt berechnen
note1 = 15
note2 = 16
note3 = 20
l = [note1, note3, note3]
s = sum(l) / 3
print("Mein Durchschnitt ist: ", s)


# Kilometer in Meilen umrechnen
# Umrechnungsfaktor: 1 Kilometer = 0.621371 Meilen
f = 0.621371

# Den Nutzer nach der Kilometeranzahl fragen
km = float(input("Wie viele Kilometer möchtest du umrechnen? "))


print("Umrechnung in Meilen: ", km * f)
