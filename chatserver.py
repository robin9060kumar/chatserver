# Importing Required Modules
import socket as s
import threading as thd
import os

print("\t\t\t\tWelcome to Robin's ChatApp")
print("\t\t\t\t---------------------")

# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = "192.168.43.159"
skt.bind((localIP, 1234))

# Get Partner's IP to chat with
usrIP = "192.168.43.55"
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "exit":
            print("Person is Offline!")
            os._exit(1)
        print("\n\t\t\t\t\t\t\t\t\t\t\t" + msgRcv[1][0] + ": " + msgRcv[0].decode())


# Function to Send the Message
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, 1234))
        if data.decode() == "exit":
            os._exit(1)

# Thread for Send Message Function
send_thd = thd.Thread(target=send_msg)

# Threads for Recieve Message Function
rcv_thd = thd.Thread(target=recv_msg)

# Starting Threads
send_thd.start()
rcv_thd.start()