print("Hello Papenburg!")

# Variablen

a = 0
b, c = 3.14, "Keks"
print(a, b, c)  # -> 0 3.14 Keks

# Datentypen

a = 1
print(type(a))  # -> <class 'int'> -> a ist eine ganze Zahl

b = 2.718
print(type(b))  # -> <class 'float'> -> b ist eine Dezimalzahl

c = "Känguru"
print(type(c))  # -> <class 'str'> -> c ist ein String

# Es gibt noch viele andere Datentypen, z.B.:
# - bool (Wahrheitswert) (True oder False)
# - list (Liste)
# - tuple (Tupel)
# - dict (Dictionary)
# - set (Menge)
# - ...

# Operatoren
# +, -, *, / kennt man
# // -> ganzzahlige Division -> es wird abgerundet
# % -> Modulo -> Rest einer Division (z.B. 5 % 2 = 1 oder 10 % 3 = 1 oder 9 % 3 = 0)
# ** -> Potenz

# Funktionieren (meistens) nicht mit verschiedenen Datentypen
# print("Keks" + 3) -> TypeError

# Ausnahme: z.B. int + float -> float
print(2 + 3.14)  # -> 5.14

# Bedingungen
a = 5
if a > 3:  # Falls a größer als 3 ist
    print("a ist größer als 3")  # dann gib ... aus
elif a == 3:  # Falls a nicht größer als 3 ist, überprüfe ob a gleich 3 ist
    print("a ist gleich 3")  # dann gib ... aus
else:  # Wenn keine der obigen Bedingungen zutrifft
    print("a ist kleiner als 3")  # dann gib ... aus

# aufgabe: fizzbuzz

# While Schleife

a = 0
while a < 5:  # Solange a kleiner als 5 ist
    print(a)  # gib a aus
    a += 1  # erhöhe a um 1

# Aufgabe:
# Alle Zahlen von 1 bis 10 nacheinander ausgeben (rückwärts, in zweierschritten, ...)

# Kleiner Tipp:
print(1) # -> neue Zeile
print(2, end="") # -> keine neue Zeile

# Aufgabe:
# Folgendes Muster ausgeben:
# 1
# 22
# 333
# 4444
# ...
# bis 9
