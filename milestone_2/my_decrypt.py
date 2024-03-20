def decrypt(encrypted_message, key):
    decrypted_message = ""

    for symb in encrypted_message:
        if symb.isalpha():
            is_upper = symb.isupper()            
            shifted_symb = chr((ord(symb) - key - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            decrypted_message += shifted_symb
        else:
            decrypted_message += symb
    return decrypted_message

if __name__ == "__main__":
    encrypted_message = input("Enter the message to decrypt: ")
    decryption_key = int(input("Enter the decryption key: "))
    decrypted_result = decrypt(encrypted_message, decryption_key)
    print("Decrypted message:", decrypted_result)