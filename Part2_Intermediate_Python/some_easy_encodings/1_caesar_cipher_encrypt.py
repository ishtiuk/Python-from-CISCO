
def caesar_cipher_encrypt(text):
    text = text.upper()
    cipher = ''

    for char in text:
        if not char.isalpha():
            continue
        code = ord(char) + 2

        if code > ord('Z'):
            code = ord('A')

        cipher += chr(code)

    return cipher


usr = input("Enter your sms: ")
print(f"'{usr}' caesar_cipher encoded format: {caesar_cipher_encrypt(usr)}")
