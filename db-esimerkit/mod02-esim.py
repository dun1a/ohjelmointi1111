import math

# syötteen lukeminen
name = input("Anna nimesi: ") # -> without anything in sulut, whatever you put here you have to write it yourself in output
# name = "Donya"
# / on the other side means escape-merkki
print("Moi " + name)

age = "19" # in this situation you have to put a word in the middle of "" for pritn komento to work
print("Ikäsi on " + age)

age = 5 + 7
print(age)

age = 5 + 7
str(age) # muutetaan int (kokonaisluku) -> string, esim. 8 (the summa of age) -> "8"
# print("ikäsi on vuoden päästä " + age) # tämä ei silti toimi

age = 5 + 7
age = str(age)
print("ikäsi on vuoden päästä " + age)

age = 5 + 7
age_string = str(age)
print("ikäsi on vuoden päästä " + age_string)
age = age + 1
# toinen tapa, tehdään tyyppimuunnos vain tarvittavaan kohtaan
print("ikäsi on vuoden päästä " + str(age))


age = int(age) + 7 # "7" -> 7
age_string = str(age)
print("ikäsi on vuoden päästä " + age_string)
age = age + 1

print("ikäsi on vuoden päästä " + str(age))

# käytäjän pituus metreinä, liukuluku (float)
height = 1.8 # kannattaa laittaa . pilkun tilalle, koska sitten menee suluissa
print("Pituus: " + str(height))

# height = 1.8
# height = input("Anna pituus: ")
height = float(input("Anna pituus: "))
#kasvatetaan käyttäjän 10 cm
height = height + 0.1
# f string muodossa ei tarvitse str()-funktiota
print(f"Nimi: {name}, Ikä: {age}, Pituus: {height} metriä")

print(math.pi)

# t. 6 maybe , satunnaisen kokonaisluvun arpominen 1-6 (not tehtävä, but eximerkki)
random_number = random.randint(1, 6)
# OTHER TEHTÄVÄ print(f"Satunnainen luku 1-6: {random_number}")
print(f"Satunnainen luku 1-6: {random_number}")

