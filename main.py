from sys import exit



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
                


print(ip_check())