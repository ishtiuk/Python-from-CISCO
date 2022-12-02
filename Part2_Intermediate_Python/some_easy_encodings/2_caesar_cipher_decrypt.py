
def caesar_cipher_decrypt(cipher):
    cipher = cipher.upper()
    text = ''

    for char in cipher:
        if not char.isalpha():
            continue
        code = ord(char) - 2

        if code < ord('A'):
            code = ord('Z')

        text += chr(code)

    return text


usr = input("Enter your sms: ")
print(f"'{usr}' caesar_cipher encoded format: {caesar_cipher_decrypt(usr)}")