# i = iteraattori

def is_prime_number(num):
    result = True
    for i in range(2,num):
        print(i)
        if num % i == 0:
            result = False  # jos jaollinen välillä 1-3 esim.
            break # tai return False (tämä heti lopettaa turhan rullauksen (2 numerolla voi jakaa monet numerot sen takia tiedetään heti ettei se ole alkuluku)
    return False

# testataan funtkion toimintaa erilaisilla arvoilla
print(is_prime_number(4))
print(is_prime_number(7))

def is_prime_number(num):
    if num < 1:
        return False
    for i in range(2,num):
        #print(i)
        if num % i == 0:
            return False
    return True

# pääohjelma lukee syötteen ja tulostaa vastauksen
user_input = int(input('Anna testattava luku (>0): '))
result = is_prime_number(user_input)
if result == True:
    print(f'Luku {user_input} on alkuluku')
else:
    print(f'Luku {user_input} ei ole alkuluku')



