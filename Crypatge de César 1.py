msgIn = str(input("Message à crypter : "))
key = int(input("Entrez une clé :"))
msgOut = ""
for i in (msgIn) :
    car = ord(i)
    if (car == 0):
        msgOut += chr(car)

    if (car >= 97) and (car <= 122):
        car = car - 97
        car += key
        car = car % 26
        car += 97

        msgOut += chr(car)



print(msgOut)





