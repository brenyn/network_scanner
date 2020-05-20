#!/usr/bin/env python

##########################################################################################################
#
# Author: Brenyn Kissoondath
# Course: Learn Python and Ethical Hacking From Scratch - StationX
# Instructor: Zaid Al Quraishi
# Purpose: 
# Input(s): 
# Output(s): 
#
# Notes to self: 
#
##########################################################################################################

import os
import scapy.all as scapy

def scan(ip):
	scapy.arping(ip)

scan("10.0.2.1/24")