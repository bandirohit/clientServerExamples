import socket

port = 12345

while True:
    s = socket.socket()
    s.connect(('127.0.0.1', port))
    try:
        mode = raw_input('Input:')
    except ValueError:
        print "Not a number"
    s.send(mode)
    if mode == "exit":
        break
    s.close()