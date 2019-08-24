from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
import MFRC522
import signal
MIFAREReader = MFRC522.MFRC522()
api = ApiClient(token = 'your api token')
var = api.get_variable('variable key')
price = 0
a = 0
b = 0
c = 0
d = 0
e = 0
while 1 :
    while 1:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK :
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            p1 = [46,68,219,115,194]
            p2 = [133,124,199,115,77]
            p1 = [194,86,97,163,86]
            p1 = [134,237,216,115,192]
            p5 = [110,251,213,115,51]
            if(uid == p1 and a==0):
                price = price+100
                print(uid)
                print(price)
                response = var.save_value({"value":price})
                a=a+1
                if(a==1):
                    break
            if(uid == p2 and b==0):
                price = price+200
                print(uid)
                print(price)
                response = var.save_value({"value":price})
                b=b+1
                if(b==1):
                    break
            if(uid == p3 and c==0):
                price = price+500
                print(uid)
                print(price)
                response = var.save_value({"value":price})
                c=c+1
                if(c==1):
                    break
            if(uid == p4 and d==0):
                price = price+800
                print(uid)
                print(price)
                response = var.save_value({"value":price})
                d=d+1
                if(d==1):
                    break
            if(uid == p5 and e==0):
                price = price+1000
                print(uid)
                print(price)
                response = var.save_value({"value":price})
                e=e+1
                if(e==1):
                    break
