from aes import AES

while True:
    mode = input('Select AES mode (E: Encryption, D: Decryption)\nor Enter Q to quit\nSelection: ')
    if mode == 'Q' or mode == 'q':
        break

    elif mode == 'E' or mode == 'e':
        key = input('Enter the key in hex: ')
        plain = input('Enter the plain text in hex: ')
        aes = AES(key=key, plain=plain)
        aes.encrypt()
        print('Cipher text: ')
        print(aes.cipher)

    elif mode == 'D' or mode == 'd':
        key = input('Enter the key in hex: ')
        cipher = input('Enter the cipher text in hex: ')
        aes = AES(key=key, cipher=cipher)
        aes.decrypt()
        print('Plain text: ')
        print(aes.plain)

    print()

# key = 2B7E151628AED2A6ABF7158809CF4F3C
# plain = 3243F6A8885A308D313198A2E0370734
# cipher = 3925841D02DC09FBDC118597196A0B32
