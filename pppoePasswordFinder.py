from scapy.all import *

homeRouterMac = "3E:84:0B:62:08:F4" #Find via wireshark
buildingRouterMac = "8C:F5:F4:11:B0:18" #Find via wireshark

homeRouterInterface = "en8" #Find via wireshark
buildingRouterInterface = "en6" #Find via wireshark

def forwardPacketToBuildingRouter(packet: Packet):
    if(packet.getfieldval("src") == homeRouterMac):
        print(packet)
        sendp(packet, iface=buildingRouterInterface)

def forwardPacketToHomeRouter(packet: Packet):
    if(packet.getfieldval("src") == buildingRouterMac):
        sendp(packet, iface=homeRouterInterface)

def sniff_interface(iface, prn):
    sniff(iface=iface, prn=prn, store=0)

thread1 = threading.Thread(target=sniff_interface, args=(homeRouterInterface, forwardPacketToBuildingRouter))
thread2 = threading.Thread(target=sniff_interface, args=(buildingRouterInterface, forwardPacketToHomeRouter))

thread1.start()
thread2.start()