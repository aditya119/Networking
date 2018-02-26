import socket
import sys
from uuid import getnode as get_mac


class Packet:

    def __init__(self, payload, receiverIP, receiverMAC, packet_sequence_number, certificate=''):
        self.payload = payload
        self.receiverIP = receiverIP
        self.receiverMAC = receiverMAC
        self.senderIP = socket.gethostbyname(socket.gethostname())
        self.senderMAC = get_mac()
        self.senderMAC = ':'.join(("%012X" % self.senderMAC)[i:i + 2] for i in range(0, 12, 2))
        self.certificate = certificate
        self.packet_sequence_number = packet_sequence_number

    def create_packet(self):
        packet_dict = {'payload': self.payload, 'sender_ip': self.senderIP, 'sender_mac': self.senderMAC,
                       'receiver_ip': self.receiverIP, 'receiver_mac': self.receiverMAC,
                       'certificate': self.certificate, 'seq_no': self.packet_sequence_number}
        return packet_dict


def write_binary_data_to_file(packet_list):
    reg_pac = bytes()
    for p in packet_list:
        reg_pac += p
    out_file = input('enter output file name:')
    file_out = open(out_file, 'wb')
    file_out.write(bytes(reg_pac))
    file_out.close()


def retrieve_packets(packet_list):
    reg_pac = bytes()
    for p in packet_list:
        print('packet number: ' + str(p['seq_no']) + ' size ' + str(sys.getsizeof(p)))
        reg_pac += p['payload']
    out_file = input('enter output file name:')
    file_out = open(out_file, 'wb')
    file_out.write(bytes(reg_pac))
    file_out.close()


def input_file(receiver_ip):
    filename = input('enter file name:')
    file = open(filename, 'rb')
    byte_string = file.read()
    file_size = len(byte_string)
    print(str(file_size) + ' bytes')
    file.close()

    packet_size = int(input('enter packet size in bytes (max 1024):'))
    print(str(int(file_size / packet_size)) + ' packets with payload size ' + str(packet_size), end=' ')
    if file_size % packet_size != 0:
        print('one packet with payload size', str(file_size % packet_size))
    else:
        print()
    packets = []

    for i in range(0, len(byte_string), packet_size):
        p = Packet(byte_string[i:i + packet_size], receiver_ip, '6A:7B:56:38:49:5A', int(i / packet_size), '0001')
        packets.append(p.create_packet())
    return packets
