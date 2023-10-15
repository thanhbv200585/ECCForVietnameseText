import json

def main():
    # char = input('Enter character: ')
    # read_chars(char)
    print("Result: " , base3_to_decimal("22222"))

def read_chars(char):
    if char == "Â":
        print("Â")
    else: 
        print("unrecognized character")

def decimal_to_base3(decimal_num):
    if decimal_num == 0:
        return '0' * 5
    
    base3_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 3
        base3_num = str(remainder) + base3_num
        decimal_num //= 3
    base3_num = base3_num.rjust(5, '0')
    return base3_num

def base3_to_decimal(base3_num):
    if len(base3_num) != 5:
        raise ValueError("Invalid base 3 number. It must have exactly 5 digits.")
    
    decimal_num = 0
    for digit in base3_num:
        decimal_num = decimal_num * 3 + int(digit)
    
    return decimal_num

def circular_shift_left(base3_num):
    if len(base3_num) != 5:
        raise ValueError("Invalid base 3 number. It must have exactly 5 digits.")
    
    return base3_num[1:] + base3_num[0]

def circular_shift_right(base3_num):
    if len(base3_num) != 5:
        raise ValueError("Invalid base 3 number. It must have exactly 5 digits.")
    
    return base3_num[-1] + base3_num[:-1]

def character_to_pair(character, mapping):
    return mapping.get(character.upper(), ('Invalid', 'Invalid'))

with open("alphabet.json", "r") as file:
    mapping = json.load(file)
input_string = input("Enter string: ")
pairs = []

for character in input_string:
    pair = character_to_pair(character, mapping)
    pairs.append(pair)

print("Pairs:", pairs)

if __name__ == "__main__":
    main()