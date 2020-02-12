
import socket
import threading
def connectToServer(hostName):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 5010))
    print("Connection Established")
    while True:
        data = s.recv(1024) 
        print(data.decode("utf-8"))
        
        #break data down
        uid = data[0:5]
        speed = data[5:7]
        time = data[7:13]
        trainid = data[13:16]
        print("hi")
        
    
def main():
    
    portConnectingToServers = 5001
    hostNames = ["127.0.0.1"]
    #connectToServer(hostNames[0])
    for host in hostNames:
        thread = threading.Thread(target=connectToServer, args=(host,))
        thread.start()
        thread.join()

if __name__ == '__main__':
    main()


























    