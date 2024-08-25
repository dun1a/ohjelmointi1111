# kirjoita ohjelma, joka kysyy ympyrän säde ja tulostaa sen pinta-alaa
# pii*r^2
import math
import random

r = float(input("Anna ympyrän säde (m): "))

area = math.pi * r * r
print(area)

# tai

print(f"Ympyrän säde on {r}, pinta-ala on {area} neliömetreinä")
print(f"Ympyrän säde on {r}, pinta-ala on {area:.1f} neliömetreinä") # area:.1f pyöristi numeron yhden tarkkuudelle -> 28.3