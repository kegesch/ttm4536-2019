import sys
import socket
import getopt
import threading
import subprocess
import time
from Crypto import Random

target_host = "129.241.200.165"
target_port = 2200
# create a socket object

# connect the client

if "ttm4536" in str(b"ttm4536"):
    print("works")

try:

    # send some data
    # receive some data

    for i in range(100000000):
        print(str(i)+"\n")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_host, target_port))
        msg = Random.get_random_bytes(10**i) + "\n"
        #print(msg)
        client.send(bytes(msg))

        recv_len = 1
        response = ""

        while recv_len:
            time.sleep(0.1)
            data = client.recv(1024)
            recv_len = len(data)
            response += str(data)

            if recv_len < 1024:
                break
        if "ttm4536" in response:
            print(response)
            client.close()
            break

except Exception as e:
    print("[*] Exception! Exiting " + str(e))
    client.close()