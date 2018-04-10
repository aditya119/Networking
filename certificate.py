from node import *

host = socket.gethostbyname(socket.gethostname())
port = 9997

with open('certificate.txt') as file:
    content = file.readlines()
file.close()

client_list = {}

for c in content:
    client_list = eval(c)

print(client_list)
certificate_socket = Node(host, port)

certificate_socket.act_as_server()

while True:
    print(certificate_socket.send_certificate(client_list))
    print('\n\n\n\n')
    input('y/n')