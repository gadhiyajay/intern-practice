def encrypt_func(txt, s):
    result = ("")

    for i in range(len(txt)):
        char = txt[i]

        if (char.isupper()):
            result += chr((ord(char) + s -64)% 26 + 65)
        else:
            result += chr((ord(char) + s -96)% 26 + 97)
    return result

txt = "JAY GADHIYA"
s = 7160
print("Plain text :", txt)
print("Shift Pattern :", str(s))
print("Cipher :", encrypt_func(txt, s))