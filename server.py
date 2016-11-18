import socket
from GPIOLibrary import GPIOProcessor

s = socket.socket()
host = socket.gethostname()
socket.getaddrinfo()

GP = GPIOProcessor()
Pin25 = 0
try:

    Pin25 = GP.getPin25()
    Pin25.out()

finally:
    GP.cleanup()


print host
port = 12345

s.bind((host,port))

print "waiting for client .."
s.listen(5)

c, addr = s.accept()

while True:
    msg = c.recv(1024)
    if(msg=="stop"):
        break
    elif(msg =="1") :
        Pin25.high()
    else:
        Pin25.low()

