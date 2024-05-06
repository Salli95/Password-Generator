import random
import string

LARGletters = string.ascii_uppercase
SMALLletters = string.ascii_lowercase
INTEGER = string.digits

print("Выберите тип пароля: \n1-смешаный\n2-численый\n3-символьный")
answer=int(input())

def mixedpassword(length):
    password = ''
    for i in range(length):
        
     if answer==1: 
      RANDchoice = random.choice([LARGletters, SMALLletters, INTEGER])
      password += random.choice(RANDchoice)
      
     if answer==2:
       RANDchoice = random.choice([INTEGER])
       password += random.choice(RANDchoice)
          
     if answer==3:
       RANDchoice = random.choice([LARGletters, SMALLletters])
       password += random.choice(RANDchoice)
              
    return password

print(mixedpassword(10))