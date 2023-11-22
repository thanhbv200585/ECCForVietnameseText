import sys
sys.path.append("..")
import json

LIST_CHAR = "aàãảáạăằẵẳắặâầẫẩấậbcdđeèẽẻéẹêềễểếệfghiìĩỉíịklmnoòõỏóọôồỗổốộơờỡởớợpqrstuùũủúụưừữửứựvxyỳỹỷýỵzAÀÃẢÁẠĂẰẴẲẮẶÂẦẪẨẤẬBCDĐEÈẼẺÉẸÊỀỄỂẾỆFGHIÌĨỈÍỊKLMNOÒÕỎÓỌÔỒỖỔỐỘƠỜỠỞỚỢPQRSTUÙŨỦÚỤƯỪỮỬỨỰVXYỲỸỶÝỴZ 0123456789 .,;?!@$%^&-+()[]{}=|<>‘:"

def find_generator_point(curve):
  p = int(curve.p)
  a = int(curve.a)
  b = int(curve.b)
  for x in range(p):
    for y in range(p):
      if (y**2 - x**3 - a*x - b) % p == 0:
        return (x, y)

def generate_mapping_table(curve):
    # Generate mapping table for characters corresponding to points on the curve
    mapping_table = {}
    generator_point = find_generator_point(curve)

    current_point = generator_point
    mapping_table[generator_point] = LIST_CHAR[0]
    for char in LIST_CHAR[1:]:
      current_point = curve.point_add(current_point, generator_point)
      mapping_table[current_point] = char
    
    return mapping_table

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

def encryption(mapping_table, plaintext, key):
    encrypted_text = ""

    for char in plaintext:
        p_i = list(mapping_table.values()).index(char) + 1
        key_int = int(key)  # Convert key to integer
        p2 = (p_i + key_int) % (len(mapping_table) + 1)
        encrypted_point = list(mapping_table.keys())[p2 - 1]
        x, y = encrypted_point
        x1 = circular_shift_right(decimal_to_base3(x))
        y1 = circular_shift_right(decimal_to_base3(y))
        # Append the sequence numbers to the encrypted text
        encrypted_text += x1 + " " + y1 + " "

    return encrypted_text.strip()


def decryption(mapping_table, encrypted_text, key):
    decrypted_text = ""
    base3_list = encrypted_text.split(" ")
    dec = [base3_to_decimal(circular_shift_left(base3)) for base3 in base3_list]  # shift left and convert base3 to decimal
    points = [(dec[i], dec[i + 1]) for i in range(0, len(dec), 2)]  # generate the list of points of ciphertext
    key_int = int(key)  # Convert key to integer
    list_c = [list(mapping_table.keys()).index(point) + 1 for point in points]  # get the list of C_i
    list_c_prime = [(p - key_int) % (len(mapping_table) + 1) for p in list_c]  #
    decrypted_text = [list(mapping_table.values())[c_prime - 1] for c_prime in list_c_prime]
    return "".join(decrypted_text)


def write_mapping_table(mapping_table, filename):
    output = {str(key) : value for key, value in mapping_table.items()}

    with open(filename, "w") as f:
        json.dump(output, f, indent=4)