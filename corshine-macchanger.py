##Author: CORSHINE
##################################################
## / ___/ _ \|  _ \/ ___|| | | |_ _| \ | | ____|##
##| |  | | | | |_) \___ \| |_| || ||  \| |  _|  ##
##| |__| |_| |  _ < ___) |  _  || || |\  | |___ ##
## \____\___/|_| \_\____/|_| |_|___|_| \_|_____|##
##################################################

import random
import os
import subprocess 

def get_rand():
    return random.choice("abcdef0123456789") 

def new_mac():
    new_ = "" 
    for i in range(0,5):
        new_ += get_rand() + get_rand() + ":"  
    new_ += get_rand() + get_rand() 
    return new_


#Changing eth0

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}")) 
subprocess.call(["sudo","ifconfig","eth0","down"]) 
new_m = new_mac() 
subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m]) 
subprocess.call(["sudo","ifconfig","eth0","up"]) 
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

#Chaning wlan0

print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}")) 
subprocess.call(["sudo","ifconfig","wlan0","down"]) 
new_m = new_mac() 
subprocess.call(["sudo","ifconfig","wlan0","hw","ether","%s"%new_m]) 
subprocess.call(["sudo","ifconfig","wlan0","up"]) 
print(os.system("ifconfig wlan0 | grep ether | grep -oE [0-9abcdef:]{17}"))
