# нужно сделать настроку типа пароля а также его длину

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
      fhg = random.choice([LARGletters, SMALLletters, INTEGER])
      password += random.choice(fhg)
      
     if answer==2:
       fhg = random.choice([INTEGER])
       password += random.choice(fhg)
          
     if answer==3:
       fhg = random.choice([LARGletters, SMALLletters])
       password += random.choice(fhg)
              
          
    return password




print(mixedpassword(10))