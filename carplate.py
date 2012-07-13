# carplate.py

weight = [14, 2, 12, 2, 11, 1]
checksum_alphabet = ['A', 'Y', 'U', 'S', 'P', 'L', 'J', 'G', 'D', 'B', 'Z', 'X', 'T', 'R', 'M', 'K', 'H', 'E', 'C']


carplate = list(input("Input carplate number: "))

for i in carplate:
# remove first alphabet
    if carplate[0] == 'S':
        carplate_n = carplate[1:-1]
# insert 0 if there are only 3 numbers
    if len(carplate_n) == 5:
        carplate_n.insert(2,'0')

checksum = 0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# convert alphabet prefixes to numbers
for i in range(0, 2):
    for e in range(0,25):
        if carplate_n[i] == alphabet[e]:
            carplate_n[i] = number_list[e]

for i in range(0,7):
    checksum = checksum + int(carplate_n[i]) * int(weight[i])
# compute checksum using modulo
    checksum = checksum % 19

def is_valid_carplate(number):
    # validate carplate number
        if checksum == carplate[-1]:
            return True
        else:
            return False
            print("Correct checksum alphabet:", checksum_alphabet[checksum])

print (is_valid_carplate(carplate))


##if is_valid_carplate(carplate) is False:
##    try: 
##        outfile = open("INVALID.DAT", "w")
##        outfile.write(carplate + "\n")
##    except Error:
##        print("Cannot write to file 'INVALID.DAT'")
##
