def dec(encoded):
    temp_pass = ""
    for x in range(len(encoded)):
        temp_pass += str(int(encoded[x]) - 3)
    return temp_pass
