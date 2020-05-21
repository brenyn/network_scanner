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
	print(arp_request.summary())
	scapy.ls(scapy.ARP())# scapy.ls returns all variables contained in ARP class

scan("10.0.2.1/24")