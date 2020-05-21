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
#https://scapy.readthedocs.io/en/latest/usage.html

def scan(ip):

	arp_request = scapy.ARP(pdst=ip) #create an instance of scapy ARP class
	#arp_request.show()

	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #set destination to broadcast MAC address
	#broadcast.show()

	arp_request_broadcast = broadcast/arp_request #scapy allows to combine 2 requests like this to create broadcast packet
	#arp_request_broadcast.show()

	#scapy.srp returned 2 lists, a list of addresses that answered and a list that did not answer. for this program we're only interested in the addresses that answered
	answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0] # srp function will send the packet to broadcast MAC address and check all IPs provided by ip.
	
	print("IP\t\t\tMAC Address\n-----------------------------------------")
	
	for answer in answered_list:
		print (answer[1].psrc+"\t|\t"+answer[1].hwsrc)# each answer contains 2 lists, 1 lists the request made and the second contains the response
scan("10.0.2.1/24")