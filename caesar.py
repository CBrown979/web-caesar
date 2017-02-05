import string

def alphabet_position(letter):
    nocap = string.ascii_lowercase
    cap = string.ascii_uppercase
    all_letters = string.ascii_lowercase + string.ascii_uppercase

    for c in all_letters:
        index = 0
        c = letter
        if c in nocap:
            ascii_value = ord(c)
            c = ascii_value
            index = (c- 97) % 26
        elif c in cap:
            ascii_value = ord(c)
            c = ascii_value
            index = (c - 65) % 26
        elif c not in all_letters:
            index = ord(c)
        return index

def rotate_character(char, rot):
    c = char
    c = alphabet_position(c)
    rotation = (c + rot) % 26
    if char in string.ascii_lowercase:
        new_char = rotation + 97
        rotation = chr(new_char)
    elif char in string.ascii_uppercase:
        new_char = rotation + 65
        rotation = chr(new_char)
    elif char == char:
        rotation = char
    return rotation


def encrypt(text, rot):
    enc_cypher = []
    for m in text:
        position = rotate_character(m, rot)
        enc_cypher.append(position)
    response = ''.join(enc_cypher)
    return response
