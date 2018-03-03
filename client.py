from packet import *
from node import *


host = '192.168.178.38'
port = 9999

s = Node(host, port)

s.act_as_client()

packets = s.receive_packets()

if s.verify_packets(packets, '0001'):
    print('writing packets to file')
    retrieve_packets(packets)
else:
    print('certificate not verified, discarding packets')