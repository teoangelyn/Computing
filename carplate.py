# carplate.py
# Author: A Teo
# Date: 13 July 2012
# Program to validate car plate numbers and output invalid car plate numbers to a file

entry = input("Input carplate number in uppercase: ")
carplate = list(entry)

def check_digit_carplate(carplate):
    for i in carplate:    
    # remove first alphabet if carplate starts with 'S'
        if carplate[0] == 'S':
            del carplate[0]
            
    # remove last alphabet
    carplate = carplate[0:-1]

    # insert 0 before first numerical digit if there are only 3 numbers
    if len(carplate) == 5:
        carplate.insert(2,'0')
        
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
               17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    # convert alphabet prefixes to numbers
    for a in range(0, 2):
        for e in range(0, 25):
            if carplate[a] == alphabet[e]:
                carplate[a] = number_list[e]

 
    # initialise weights
    weights = [14, 2, 12, 2, 11, 1]
    # initialise sum of products
    sum_of_products = 0

    for i in range (0, len(weights)):
        # compute sum of products
        sum_of_products = sum_of_products + int(carplate[i]) * weights[i]
    # compute checksum using modulo
    return sum_of_products % 19

def is_valid_carplate(carplate):
    checksum_alphabet = ['A', 'Y', 'U', 'S', 'P', 'L', 'J', 'G', 'D', 'B', 'Z', 'X', 'T', 'R', 'M', 'K', 'H', 'E', 'C']
    # validate carplate number
    if checksum_alphabet[check_digit_carplate(carplate)] == list(entry)[-1]:
        return True
    else:
        return False

if is_valid_carplate(carplate) is False:
    checksum_alphabet = ['A', 'Y', 'U', 'S', 'P', 'L', 'J', 'G', 'D', 'B', 'Z', 'X', 'T', 'R', 'M', 'K', 'H', 'E', 'C']

    print("Invalid carplate number. Correct checksum alphabet: ", checksum_alphabet[check_digit_carplate(carplate)])
    try: 
        outfile = open("INVALID.DAT", "w")
        outfile.write(carplate + "\n")
    except IOError:
        print("Cannot write to file 'INVALID.DAT'")
else:
    print("Valid carplate number")

is_valid_carplate(carplate)
