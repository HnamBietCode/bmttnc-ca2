class CaesarCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = key % 26
                code = ord(char) + shift
                if char.islower():
                    if code > ord('z'):
                        code -= 26
                    encrypted_text += chr(code)
                elif char.isupper():
                    if code > ord('Z'):
                        code -= 26
                    encrypted_text += chr(code)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, key):
        return self.encrypt(text, -key)