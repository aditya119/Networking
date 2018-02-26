from packet import *

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

while True:
    packets = []
    # establish a connection
    clientsocket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))
    packets = input_file(addr)
    number_of_packets = str(len(packets))
    print('message:', number_of_packets.encode('ascii'))
    clientsocket.send(number_of_packets.encode('ascii'))
    for packet in packets:
        print("Got a connection from %s" % str(addr))
        print('certificate:', packet['certificate'])
        clientsocket.send(packet['certificate'].encode('ascii'))
        print('message:', packet['payload'])
        clientsocket.send(packet['payload'])
    clientsocket.close()
    print('\n\n\n\n')