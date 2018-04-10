from packet import *
from node import *


sender_host = socket.gethostbyname(socket.gethostname())
sender_port = 9999

receiver_host = socket.gethostbyname(socket.gethostname())
receiver_port = 9998

receive_socket = Node(sender_host, sender_port)
forwarding_socket = Node(receiver_host, receiver_port)

receive_socket.act_as_client()

packets = receive_socket.receive_packets()

forwarding_socket.act_as_server()
forwarding_socket.send_packets(packets)