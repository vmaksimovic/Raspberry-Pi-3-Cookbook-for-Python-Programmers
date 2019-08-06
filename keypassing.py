#! /usr/bin/python3
#keypassing.py
import encryptdecrypt as ENC

KEY1 = 20
KEY2 = 50

print("Please enter text to scramble:")
#Get user input
user_input = raw_input()
#Send msg out
encodedKEY1 = ENC.encryptText(user_input,KEY1)
print("USER1: Send msg encrtypted with KEYT1 (KEY1): "+encodedKEY1)
#Recive msg 
encodedKEY1KEY2 = ENC.encryptText(encodedKEY1,-KEY1)
print("USER2: ENCRTYPT with KEY2 and returns it (KEY1+KEY2) "+encodedKEY1KEY2)
#remove original encoding
encodedKEY2 = ENC.encryptText(encodedKEY1KEY2,-KEY2)
print("USER1: removes KEY and returns with just KEY2 (KEY2) "+encodedKEY2)

#reciver removes their encrypt
message_result = ENC.encryptText(encodedKEY2,-KEY2)
print("USER2: Removes KEY2 and message recived: "+message_result)
#END
