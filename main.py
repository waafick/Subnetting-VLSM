import os
import sys
import netaddr
import ipaddress
import socket



def main() -> None:
    ...


def ip_notation() : # notation : CIDR or Subnet mask
    ...


def ip_check() -> list  :

    while True :
        ip = input("Ip address format x.x.x.x : ").split(".")
        if len(ip) != 4 :
            print("Invalid ip address")
        else :
            for numbers in ip :
                if int(numbers) in range(0,256) :
                    return(ip)
                

def binary_operations() -> list :
    ...
                


print(ip_check())