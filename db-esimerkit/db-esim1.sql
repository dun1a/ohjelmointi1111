-- luodaan paikallinen käyttäjä "python"
CREATE USER python@localhost IDENTIFIED BY 'salakala';

-- Pistetaan tietokanta, jos en on jo olemassa
DROP DATABASE IF EXISTS ankkalinna;

-- luodaan ankkalinnatietokanta
CREATE DATABASE ankanlinna;

-- Annetaan käyttäjälle luku- ja päivytysoikeudet tietokantaan ankkalinna
GRANT SELECT, INSERT, UPDATE ON ankkalinna. * TO python@localhost;

# Nimen kysyminen
Käyttäjä = input("Anna nimesi: ")
print("Hauska tavata," + Käyttäjä + "!")

# kysytään ympyrän säde
numero = input("Anna ympyrän säde: ")
print(" ")

eka = 5
toka = 7
kolmas = 8
summa = eka + toka + kolmas
print"2 + 4" + ("summa")