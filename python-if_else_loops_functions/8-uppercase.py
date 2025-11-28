def uppercase(str):
    result = ""
    for c in str:
        # Check if character is lowercase a–z
        if ord('a') <= ord(c) <= ord('z'):
            # Convert to uppercase by subtracting 32
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
