#CESAR

def Cesar(msgIn, key):
  msgOut=""
  for i in msgIn:
    car=ord(i)
    if(car>=97)and(car<=112):
      car=car-97
      car+=key
      car=car%26
      car+=97
      msgOut+=chr(car)
    else:
      msgOut+=chr(car)
  print(msgOut)
    
msg=input("donner un message :")
key=int(input("Entrez une clé : "))
cod=input("Souhaitez-vous coder ou décoder[c/d]:")
if cod=="c":
       Cesar(msg,key)
else:
  Cesar(msg,26-key)

  



