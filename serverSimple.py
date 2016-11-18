import socket

s = socket.socket()

port = 12555

s.bind(('',port))

s.listen(5)
print "waiting for client"
c,addr = s.accept()
print "client connected"
while True:
    msg = c.recv(1024)
    print msg
    if msg == "exit":
        c.close()
        break