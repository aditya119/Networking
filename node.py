import socket
import time
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
        """
        the function is used to send packets over the network, the packets are edited before sending
        :param packets: the receiver address in the packets is set in this function
        """
        client_socket, client_address = self.node_socket.accept()
        print("Got a connection from", client_address)
        client_socket.send(str(len(packets)).encode('ascii'))
        for packet in packets:
            packet['receiver_ip'] = client_address
            print(packet)
            client_socket.send(str(packet).encode('ascii'))
            time.sleep(1)
        client_socket.close()

    def act_as_client(self):
        self.node_socket.connect((self.ip, self.port))

    def receive_packets(self):
        number_of_packets = int(self.node_socket.recv(1024).decode('ascii'))
        packets = []
        for i in range(number_of_packets):
            string = self.node_socket.recv(1024).decode('ascii')
            packets.append(eval(string))
            del string
            time.sleep(1)
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