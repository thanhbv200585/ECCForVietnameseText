import json

def generate_mapping():
    mapping = {}
    for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        mapping[char] = { f'{i}': f"({i // 3}, {i % 3})" }
    return mapping

# Generate the character-to-pair mapping
mapping = generate_mapping()

# Write mapping to a JSON file
with open('mapping.json', 'w') as file:
    json.dump(mapping, file)

print("Mapping has been written to mapping.json.")