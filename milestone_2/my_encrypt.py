def encrypt(message, key):
    encrypted_message = ""

    for symb in message:
        if symb.isalpha():
            is_upper = symb.isupper()
            shifted_symb = chr((ord(symb) + key - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            encrypted_message += shifted_symb
            encrypted_message += symb
    return encrypted_message

if __name__ == "__main__":
    original_message = input("Enter the message: ")
    encryption_key = int(input("Enter the key: "))
    encrypted_result = encrypt(original_message, encryption_key)
    print("Encrypted message:", encrypted_result)