from packet import *
from node import *


host = socket.gethostbyname(socket.gethostname())
port = 9998

c_host = socket.gethostbyname(socket.gethostname())
c_port = 9997

client_socket = Node(host, port)
client_socket.act_as_client()
packets = client_socket.receive_packets()

certificate_socket = Node(c_host, c_port)
certificate_socket.act_as_client()
certificate = certificate_socket.receive_certificate()

if verify_packets(packets, certificate):
    print('writing packets to file')
    retrieve_packets(packets)
else:
    print('certificate not verified, discarding packets')