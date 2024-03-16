def ip_check() -> list :
    while True :
        ip = input("Ip address in format x.x.x.x : ")
        ip = ip.split('.')

        if len(ip) != 4 :
            print("Invalid ip address")
        else :
            return ip
    
   

    


print(ip_check())