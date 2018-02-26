from packet import *

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999
# connection to hostname on the port.
s.connect((host, port))
number_of_packets = s.recv(1024)
number_of_packets.decode('ascii')
print(number_of_packets.decode('ascii'))
packets = []
flag = 0
for i in range(int(number_of_packets)):
    # Receive no more than 1024 bytes
    certificate = s.recv(1024).decode('ascii')
    print('certificate verification for',certificate)
    if certificate == '0001':
        print('certified verified')
        packets.append(s.recv(1024))
        print('packet received')
    else:
        print('packet discarded',s.recv(1024))
        print('packet not received, due to wrong certificate')
        flag = 1

s.close()
if flag == 0:
    print('writing packets to file')
    write_binary_data_to_file(packets)
else:
    print('not making file because incorrect packets recieved')