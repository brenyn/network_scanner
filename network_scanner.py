#!/usr/bin/env python

##########################################################################################################
#
# Author: Brenyn Kissoondath
# Course: Learn Python and Ethical Hacking From Scratch - StationX
# Instructor: Zaid Al Quraishi
# Purpose: Create a network scanner that will return all IPs on a network w/ MAC addresses
# Input(s): Range of IP addresses to scan
# Output(s): List of corresponding MAC/IP addresses
#
# Notes to self:
#
##########################################################################################################

import scapy.all as scapy

def scan(ip):

	arp_request = scapy.ARP(pdst=ip) #create an instance of scapy ARP class
	#arp_request.show()

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set destination to broadcast MAC address
	#broadcast.show()

	arp_request_broadcast = broadcast/arp_request #scapy allows to combine 2 requests like this to create broadcast packet
	#arp_request_broadcast.show()

	answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1) # srp function will send the packet to broadcast MAC address and check all IPs provided by ip.
	print(answered_list.summary())

scan("10.0.2.1/24")