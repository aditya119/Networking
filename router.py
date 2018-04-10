from packet import *
from node import *


sender_host = socket.gethostbyname(socket.gethostname())
sender_port = 9999

receiver_host = socket.gethostbyname(socket.gethostname())
receiver_port = 9998

receive_socket = Node(sender_host, sender_port)
forwarding_socket = Node(receiver_host, receiver_port)

receive_socket.act_as_client()

forwarding_socket.act_as_server()

number_of_packets = receive_socket.receive_number_of_packets()
client_socket, client_address = forwarding_socket.node_socket.accept()
forwarding_socket.send_number_of_packets(number_of_packets, client_socket)
for i in range(number_of_packets):
    packet = receive_socket.receive_packet(i)
    forwarding_socket.send_packet(packet, client_socket, client_address)

client_socket.close()
# forwarding_socket.send_packets(packets)