class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        num_rows = len(text) // key
        num_columns = key

        decrypted_text = [''] * num_rows

    # Fill the decrypted_text with characters from the ciphertext
        col = 0
        row = 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            if row == num_rows:
                row = 0
                col += 1

        # Join the columns to get the final decrypted text
        return ''.join(decrypted_text)

        
