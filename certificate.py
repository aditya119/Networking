from node import *
import random

host = socket.gethostbyname(socket.gethostname())
port = 9997

with open('certificate.txt') as file:
    content = file.readlines()
file.close()

client_list = {}

for c in content:
    client_list = eval(c)

for key in client_list.keys():
    client_list[key] = '000'+str(random.randint(1,9))
    
print(client_list)
certificate_socket = Node(host, port)

certificate_socket.act_as_server()

while True:
    print(certificate_socket.send_certificate(client_list))
    print('\n\n\n\n')
    input('y/n')
