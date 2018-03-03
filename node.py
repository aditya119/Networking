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
        print("Got a connection from", client_address)
        client_socket.send(str(len(packets)).encode('ascii'))
        for packet in packets:
            print(packet)
            client_socket.send(str(packet).encode('ascii'))
        client_socket.close()

    def act_as_client(self):
        self.node_socket.connect((self.ip, self.port))

    def receive_packets(self):
        number_of_packets = int(self.node_socket.recv(1024).decode('ascii'))
        packets = []
        for i in range(number_of_packets):
            string = self.node_socket.recv(1024).decode('ascii')
            # print(string)
            packets.append(eval(string))
        return packets

    def verify_packets(self, packets, certificate):
        result = True
        for packet in packets:
            if packet['certificate'] == certificate:
                print('certificate verified for packet number', packet['seq_no'])
            else:
                print('certificate does not match for packet number', packet['seq_no'])
                result = False
        return result