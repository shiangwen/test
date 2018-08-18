def caesar_cipher(str):
    new = ""
    num = -4
    for i in range(len(str)):
        order = ord(str[i])
        after = order + num
        after = ((after + 26) - 122) % 26 + 96
        if after == 96:
            after = 122
        new += chr(after)
    return new
