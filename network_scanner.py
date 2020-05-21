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
	
	client_list = []

	for answer in answered_list:
		client_dict = {'ip':answer[1].psrc , 'mac':answer[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_result(result_list):
	print("IP\t\t\tMAC")
	for result in result_list:
		print(result["ip"] + "\t\t" + result["mac"])

scan_result = scan("10.0.2.1/24")

print_result(scan_result)