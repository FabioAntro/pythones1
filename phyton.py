import math
print("Calcoliamo il perimetro di una delle seguenti figure geometriche:")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")
scelta = int(input("Inserisci la tua scelta:"))
if scelta == 1:
    lato=float(input("Inserisci la lunghezza del lato del quadrato:"))
    print("Il perimetro del quadrato è:", lato * 4)
elif scelta == 2:
    base=float(input("Inserisci la base del rettangolo: "))
    altezza=float(input("Inserisci l'altezza del rettangolo: "))
    print("Il perimetro del rettangolo é:", 2* base + 2 *altezza)
elif scelta ==3:
    raggio=float(input("Inserisci il valore del raggio: "))
    print("La circonferenza del cerchio é:", 2 * math.pi * raggio)