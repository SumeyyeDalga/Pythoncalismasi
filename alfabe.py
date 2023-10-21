
def ceaser(message):
    encrypted_message = " "


    alphabet = ["0","1","2","3","4","5","6","7","8","9"]



    for i in message:


        if i not in alphabet:
            encrypted_message +=i

        else:
            encrypted_message += alphabet[(alphabet.index(i)+2) % len(alphabet)]

    print(encrypted_message)

shift = input("Shift value: ")
ceaser(shift)