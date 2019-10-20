import socket
import cv2
import random
import time
import numpy as np
import argparse
parser = argparse.ArgumentParser(description = 'use your raspberry pi to make a security camera')
parser.add_argument('--port', nargs = '?', const = 1234, type = int, help = 'the port you want to use(default as 1234)')
parser.add_argument('--c', nargs = '?', const = 1, type = int, help = 'the integer use to VideoCapture usually 1, sometimes 0, vary by system')
args = parser.parse_args()
port = args.port
# get raspberry pi's own ip
ip = socket.gethostbyname(socket.gethostname())
# connect to the camera
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print('try changing --c to 0')
    quit(1)
while True:
    try:
        #try to connect to client
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        s.bind((ip, port))
        s.listen(5)
        c,addr = s.accept()
        #making sure the client is ready
        while True:
            msg = c.recv(1024)
            if msg == b'ready':
                c.send(b'start')
                break
        while True:
            ret,img = cap.read()
            f = cv2.imencode('.png',img)[1].tostring()
            # making sure the client is on the same pace
            c.send(b'start')
            c.sendall(f)
            c.send(b'done')
    except BrokenPipeError as err:
        print('client closed')
    else:
        break
