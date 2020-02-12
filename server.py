# import socket programming library 
import socket 


def main(): 
    
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind((socket.gethostname(), 5001))
    # s.listen(5)

    message = "23423423435645647696"
    print(socket.gethostname())
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.bind((HOST, PORT))
            s.bind((socket.gethostname(), 5001))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    data = data.decode("utf-8")
                    if not data:
                        break
                    if len(data) ==16:
                        print(data)
                        # speed = int(message[5:7])+5
                        message=data
                    # if data in "speedDown":
                        # print(data)
                        # speed = int(message[5:7])-5
                        # message=message[0:5]+str(speed)+data[7:16]

                    conn.sendall(bytes(message,"utf-8"))
            
            
    # a forever loop until client wants to exit 
    
    # with conn:
        # print('Connected by', addr)
        # while True:
            # data = conn.recv(1024)
            # if not data:
                # break
            # conn.sendall(data)
            
        # clientsocket, address = s.accept()
        # print(f"Connection from {address} has been established.")
        # while True:
            # clientsocket.send(bytes(message,"utf-8")) 
                
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.connect((socket.gethostname(), 5001))
        # s.sendall(bytes(message,"utf-8"))
        # data = s.recv(1024)

if __name__ == '__main__': 
    main() 
