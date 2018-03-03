from packet import *
from node import *

host = '192.168.178.38'
port = 9999

server_socket = Node(host, port)

server_socket.act_as_server()

while True:
    packets = input_file(host, get_mac(), 'tobedone', get_mac())
    server_socket.send_packets(packets)
    print('\n\n\n\n')