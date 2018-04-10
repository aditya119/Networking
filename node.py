import socket
from uuid import getnode as get_mac


class Node:
    def __init__(self, ip, port):
        self.node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def act_as_server(self):
        self.node_socket.bind((self.ip, self.port))
        self.node_socket.listen(5)

    def send_packets(self, packets):
        client_socket, client_address = self.node_socket.accept()
        print("Got a connection from", client_address[0])
        client_socket.send(str(len(packets)).encode('ascii'))
        for packet in packets:
            packet['sender_mac'] = get_mac()
            packet['receiver_ip'] = client_address[0]
            print(packet)
            client_socket.send(str(len(str(packet))).encode('ascii'))
            client_socket.send(str(packet).encode('ascii'))
        client_socket.close()

    def act_as_client(self):
        self.node_socket.connect((self.ip, self.port))

    def receive_packets(self):
        number_of_packets = int(self.node_socket.recv(7).decode('ascii'))
        packets = []
        for i in range(number_of_packets):
            packet_size = int(self.node_socket.recv(3).decode('ascii'))
            print('packet number ' + str(i + 1) + ' size', packet_size)
            string = self.node_socket.recv(packet_size).decode('ascii')
            packets.append(eval(string))
            del string
        return packets

    def send_certificate(self, client_list):
        client_socket, client_address = self.node_socket.accept()
        print("Got a connection from", client_address)
        if client_address[0] not in client_list.keys():
            return 'client doesnt exist on certificate server'
        certificate_number = client_list[client_address[0]]
        print(certificate_number)
        client_socket.send(str(len(str(certificate_number))).encode('ascii'))
        client_socket.send(str(certificate_number).encode('ascii'))
        client_socket.close()
        return 'corresponding certificate number sent'

    def receive_certificate(self):
        packet_size = int(self.node_socket.recv(3).decode('ascii'))
        print('certificate size', packet_size)
        return self.node_socket.recv(packet_size).decode('ascii')


def verify_packets(packets, certificate):
    result = True
    for packet in packets:
        if packet['certificate'] == certificate:
            print('certificate verified for packet number', packet['seq_no'])
        else:
            print('certificate does not match for packet number', packet['seq_no'])
            result = False
    return result