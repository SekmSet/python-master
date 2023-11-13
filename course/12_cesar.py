# Le chiffre de César fonctionne par décalage des lettres de l'alphabet.
# Par exemple, avec une distance de 3 caractères
# B devient E dans le texte codé.

# Exemple de texte à chiffrer
# Two roads diverged in a yellow wood, And sorry I could not travel both
# And be one traveler, long I stood
# And looked down one as far as I could To where it bent in the undergrowth.

offset = 1
text = "John"

def caesar_cipher(text: str, offset: int) -> str:
    cipher = ""

    for char in text:
        if 'a' <= char <= 'z':
            ascii_code = ord(char) - ord('a')
            ascii_code = (ascii_code + offset) % 26
            cipher += chr(ascii_code + ord('a'))
            continue

        if 'A' <= char <= 'Z':
            ascii_code = ord(char) - ord('A')
            ascii_code = (ascii_code + offset) % 26
            cipher += chr(ascii_code + ord('A'))
            continue
        else:
            cipher += char

    return cipher

def caesar_decrypt(text: str) -> list[str]:
    uncipher = []

    for i in range(1,27):
        possibilities = caesar_cipher(text, i)
        uncipher.append(possibilities)

    return uncipher

result_cipher = caesar_cipher(text, offset)
result_uncipher = caesar_decrypt(text)

print(result_cipher)
print(result_uncipher)

# ord(...) : letter to ascii
# chr(...) : ascii to letter
