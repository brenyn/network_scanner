#!/usr/bin/env python

##########################################################################################################
#
# Author: Brenyn Kissoondath
# Course: Learn Python and Ethical Hacking From Scratch - StationX
# Instructor: Zaid Al Quraishi
# Purpose: Create a network scanner that will return all IPs on a network w/ MAC addresses
# Input(s): 
# Output(s): 
#
# Notes to self: problems with passing range of IPs into scapy.ARP
#
##########################################################################################################

import scapy.all as scapy

def scan(ip):

	arp_request = scapy.ARP(pdst=ip) #create an instance of scapy ARP class
	arp_request.show()

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set destination to broadcast MAC address
	broadcast.show()

	arp_request_broadcast = broadcast/arp_request #scapy allows to combine 2 requests like this.
	arp_request_broadcast.show()

	print(arp_request_broadcast.summary())
	#scapy.ls(scapy.Ether())# scapy.ls returns all variables contained in ARP class

scan("10.0.2.1/24")