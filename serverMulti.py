import socket
import thread

def clientThread(clientSocket):
    while True:
        clientMsg = clientSocket.recv(1024)
        print clientMsg
        clientSocket.close()
        '''
        if(clientMsg == "exit"):
            clientSocket.close()
            break
        else:
            print clientMsg
        '''

s = socket.socket()
port = 12345
s.bind(('',port))
s.listen(10)

while True:
    c, addr = s.accept()
    try:
        thread.start_new_thread(clientThread(c))
    except:
        print "client exited"