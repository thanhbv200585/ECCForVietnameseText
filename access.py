import json
import ast

def character_to_pair(character, mapping):
    pair = mapping.get(character.upper())
    if pair:
        return next(iter(pair.values()))
    else:
        return ('Invalid', 'Invalid')

# Example usage
input_string = input("Enter a string: ")

# Load the character-to-pair mapping from a JSON file
with open('mapping.json', 'r') as file:
    mapping = json.load(file)

pairs = []
for character in input_string:
    first, second = ast.literal_eval(character_to_pair(character, mapping))
    pairs.append(first)
    pairs.append(second)

print("Pairs:", pairs)


# 1. Input string
# 2. Convert into a pair: Mapping
# 3. Encrypt with point addition + point multiplication 
# 4. Convert into base 3
# 5. Shift to the right 1 digit
# 6. Concatenate the encypted input string then turn it into a sequence of numbers
# 7. Shift to the left 1 digit 
# 8. Decrypt with point addition + point multiplication + key
# 9. Convert point --> character.