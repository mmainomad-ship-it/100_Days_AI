# cipher.py
def main():
    print("Caesar Cipher Encoder/Decoder")

    # Get user choice
    mode = input("Do you want to (E)ncode or (D)ecode? ").upper()

    # Get necessary inputs
    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift number (e.g., 3): "))

    if mode == "E":
        # Call the encode function
        result = encode_text(text, shift)
        print(f"Encoded message: {result}")
    elif mode == "D":
        # Decoding is just encoding with a negative shift!
        result = encode_text(text, -shift)
        print(f"Decoded message: {result}")
    else:
        print("Invalid mode selection.")


def encode_text(text, shift):
    result = ""
    # Ensure shift is between 0 and 25
    shift = shift % 26
    for char in text:
        if char.isalpha():
            # Determine starting point based on case
            start_char = ord("A") if char.isupper() else ord("a")

            # 1. Convert to a 0-25 index
            relative_index = ord(char) - start_char

            # 2. Apply shift and handle wrap-around using modulo (%)
            new_index = (relative_index + shift) % 26

            # 3. Convert back to character
            new_char = chr(new_index + start_char)
            result += new_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result


if __name__ == "__main__":
    main()
