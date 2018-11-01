import socket, json, _thread
from mlpclass import mlpClassDlib, testDataMLPClass
def sendingArray(myServerAddress, myArray, myEmail):

    socko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socko.connect(myServerAddress)
    print("What is going on????",myServerAddress)
    data = '{"email" :'+ str(myEmail) + '"results" :' + str(myArray) + '}'
    print("Sending", data)
    #socko.connect(serverAddress)
    print(type(myArray))
    myArray = myArray.tolist()
    print(type(myArray))
    data = json.dumps({"email" : myEmail, "results" : myArray})
    print("Preparing to send data", data)
    print(len(data))
    #Set up the size of the data.
    sizeOfData = len(data)
    sizeOfData = str(sizeOfData)
    for i in range(20):
        sizeOfData = '0' + sizeOfData
        if len(sizeOfData) == 20:
            break
    #Sending size of 20
    print("Size of the data", int(sizeOfData))
    socko.sendall(sizeOfData.encode('utf-8'))
    print("Send json...")
    socko.sendall(data.encode('utf-8'))
    #Then I should have sent the info to the serverself.
    socko.close()

def getingArray(connection, address):

    print("Connected by ", address)
    print("Beginning Data Retrieval....")
    #Gets the data
    msgSize = connection.recv(20)
    msgSize = int(msgSize)
    data = connection.recv(msgSize)

    connection.close()
    data = data.decode('utf-8')
    print("Data Printing...")
    print(data)
    print("Data Finished...")
    data = json.loads(data)
    myEmail = data.get("email")
    myArray = data.get("results")
    print("Email", myEmail)
    print("Results",myArray)
    print("Beginning training")
    # This is for the training of an MLP Classifier.
    mlpClassDlib(myEmail)
    theMLPEmail = myEmail.replace("@","_")
    print("Generated machine learning MLP Classifier", theMLPEmail)
    print("Sending info back.")
    testNumbers = testDataMLPClass(theMLPEmail)
    myAddress = list(address)
    myAddress[1]= 5101
    myAddress = tuple(myAddress)
    print("This is the array we are sending to", myAddress)
    sendingArray(myAddress, testNumbers, theMLPEmail)

def backendSide(myEmail):
    IP = 'localhost'
    PORT = 5019
    serverAddress = (IP, PORT)
    #Server needs to set up the connections.
    serverSocko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocko.bind(serverAddress)
    serverSocko.listen(1)
    while(True):
        conn, addr = serverSocko.accept()
        #data = connection.recv(msgSize)
        currentThread = _thread.start_new_thread(getingArray, (conn, addr))
    #getingArray(conn,addr)
if __name__ == '__main__':
    IP = 'localhost'
    PORT = 5019
    serverAddress = (IP, PORT)
    A = [1,2,3,2,1]
    email = "mr@socko.com"
    #Server needs to set up the connections.
    serverSocko = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocko.bind(serverAddress)
    serverSocko.listen(1)
    while(True):
        conn, addr = serverSocko.accept()
        #data = connection.recv(msgSize)
        currentThread = _thread.start_new_thread(getingArray, (conn, addr))
    #getingArray(conn,addr)
