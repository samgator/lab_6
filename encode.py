def encode(password):
    # Sam Morsics's encode function
    encoded_password = ""

    for num in password:

        encoded_password += str((int(num) + 3))

    return encoded_password


