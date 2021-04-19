def ciphes(msg):
        translated =''
        for char in msg:
                if char >= 'a' and char <='z':
                        translated = translated + chr(219-ord(char))
                elif char >= 'A' and char <= 'Z':
                        translated = translated +chr(155 - ord(char))
                else:
                        translated = translated + char
        return translated


plaintext = 'This is something'
ciphertxt = ciphes(plaintext)
print(ciphertxt)
                        
