def process_text(text, k, encrypt=True):
    result = ""
    letter_count = 0

    for char in text:
        if char.isalpha():
            pair = letter_count // 2

            if letter_count % 2 == 0:
                shift = k + pair + 2
            else:
                shift = k + pair + 1

            if not encrypt:
                shift = -shift

            base = ord('A') if char.isupper() else ord('a')

            new_char = chr(
                (ord(char) - base + shift) % 26 + base
            )

            result += new_char
            letter_count += 1

        else:
            result += char

    return result


mode = input("Encrypt or Decrypt? (E/D): ").strip().upper()
text = input("Enter text: ")
key = int(input("Enter key: "))

if mode == "E":
    print("Encrypted:", process_text(text, key, True))
elif mode == "D":
    print("Decrypted:", process_text(text, key, False))
else:
    print("Invalid mode.")
input()
