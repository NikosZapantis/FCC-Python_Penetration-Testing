#!/usr/bin/python3

import nmap

# Creating a port scanner
scanner = nmap.PortScanner()

# Displaying welcome message
print("Welcome, this is a simple nmap automation tool")
print("<------------------------------------------------------>")

# Allows user to input the IP address they want to scan [ipconfig at cmd]
ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)

# Displaying the user the options to select the type of scan they want to run
resp = input(""" \nPlease enter the type of scan you want to run
                  1)SYN ACK Scan 
                  2)UDP Scan
                  3)Comprehensive Scan\n""")

print("You have selected option: ", resp)

# if cases for each scan option
if resp == '1':
    # IF case for SYN ACK Scan
    print("Nmap Version: ", scanner.nmap_version())

    # Performing a SYN Scan (stealth scan) on ports 1-1024 with verbose output (-v)
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # IF case for UDP Scan
    print("Nmap Version: ", scanner.nmap_version())

    # Performing a UDP Scan on ports 1-1024 with verbose output (-v)
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    # IF case for Comprehensive Scan
    print("Nmap Version: ", scanner.nmap_version())

    # Performing a comprehensive scan with multiple flags for detailed information
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    # Informing user if he provided an invalid option
    print("Please enter a valid option")