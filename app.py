# Import socket module 
import socket 

#import datetime 
from flask import Flask, render_template, jsonify ,request
import threading

app = Flask(__name__) 
global dataArray
dataArray = [{}]
#uid =''
#speed = ''
#time = ''
#trainID = ''

@app.route('/')
def index():
    """Renders the home page."""
    return render_template('index.html', title='Home Page')

@app.route('/_sendData/<data>', methods= ['GET','POST'])
def sendData(data):
    #break data down
    global dataArray
    uid = data[0:5]
    speed = data[5:7]
    time = data[7:13]
    trainID = data[13:16]
    dataArray.append({'uid': uid,'speed': speed,'time': time,'trainID': trainID})

def datatostr():
    """dict to message"""
    datamess=""
    for key, value in dataArray[0].items():
        print(key, value)
        datamess=datamess+str(dataArray[0][key])
    return datamess
    
    
@app.route('/getData',methods = ['GET','POST'])
def getData():
    global dataArray
    print(dataArray)
    data = dataArray[0]
    # del dataArray[0]
    return jsonify(data)

@app.route('/speedUp',methods = ['GET','POST'])
def speedUp():
    if request.method == "POST":
        
        speedpage = request.json['speed']
        datamessage=datatostr()
        speed = int(datamessage[5:7])+int(speedpage)
        datamessage=datamessage[0:5]+str(speed)+datamessage[7:16]
        print(speed)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((socket.gethostname(), 5001))
                s.sendall(bytes(datamessage,"utf-8"))
                data = s.recv(1024)  
                data = data.decode("utf-8")
                print(data)
                sendData(data) 
    return ('', 204)
    
@app.route('/speedDown',methods = ['GET','POST'])
def speedDown():
    if request.method == "POST":
        
        speedpage = request.json['speed']
        datamessage=datatostr()
        speed = int(datamessage[5:7])-int(speedpage)
        datamessage=datamessage[0:5]+str(speed)+datamessage[7:16]
        print(speed)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((socket.gethostname(), 5001))
                s.sendall(bytes(datamessage,"utf-8"))
                data = s.recv(1024)  
                data = data.decode("utf-8")
                print(data)
                sendData(data)     
    return ('', 204)           
def sendData(data):
    #break data down
    global dataArray
    uid = data[0:5]
    speed = data[5:7]
    time = data[7:13]
    trainID = data[13:16]
    dataArray[0]={'uid': uid,'speed': speed,'time': time,'trainID': trainID}
    print(dataArray)

def connectToServer(hostName):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((socket.gethostname(), 5001))
    # print("Connection Established ",socket.gethostname())
    # while True:
        # data = s.recv(1024)
        # data = data.decode("utf-8")
        # sendData(data)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((socket.gethostname(), 5001))
        s.sendall(b'Hello, world')
        data = s.recv(1024)  
        data = data.decode("utf-8")
        print(data)
        sendData(data)      
    # HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    # PORT = 65432        # Port to listen on (non-privileged ports are > 1023)   
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.bind((socket.gethostname(), 5001))
        # s.listen()
        # conn, addr = s.accept()
        # with conn:
            # print('Connected by', addr)
            # while True:
                # data = conn.recv(1024)
                # if not data:
                    # break
                # data = data.decode("utf-8")
                # sendData(data)

def main():
    portConnectingToServers = 5001
    hostNames = ["127.0.0.1"]
    #connectToServer(hostNames[0])
    for host in hostNames:
        thread = threading.Thread(target=connectToServer, args=(host,))
        thread.start()
        thread.join()

def runServer():
    app.run()

if __name__ == '__main__':
    host = "127.0.0.1"
    thread = threading.Thread(target=main, args=())
    thread2 = threading.Thread(target=runServer, args=())
    #app.run()
    #main()
    thread.start()
    thread2.start()
    
    


    

'''
Multiple servers -> 1 client 5001 (MAIN FUCNTION) -> information is sent to be served on port 5000
WE are building the "client" using main

Flask app is a webserver running port 5000
'''


'''
Things to do: 
1. Run Main() and Start up App Server
2. Ajax to get from server information and update page 
3. Fix index.html to look good
'''
    

"""
@socketio.on('message', namespace='/train1')
def test_message(message):
    print('Message: ' + message)

@socketio.on('connect', namespace='/train1')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print('Train1 Connected')

@socketio.on('disconnect', namespace='/train1')
def test_disconnect():
    print('Train1 disconnected' + request.namespace.socket.sessid)
"""

#@socketio.on('message')
#def handleMessage(msg):
#    print('Message: ' + msg)
  #  send(msg, broadcast=True)

