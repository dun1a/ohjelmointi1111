
max_num = -100
min_num = 100
while True:
    input_string = (input('Syötä luku: '))
    if input_string == '':
        break
    number = int(input_string)    #jos ei ole tyhä jonomerkki
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f'Pienin numero: {min_num}, suurin numero: {max_num}')
