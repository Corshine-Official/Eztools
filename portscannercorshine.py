##################################################
## / ___/ _ \|  _ \/ ___|| | | |_ _| \ | | ____|##
##| |  | | | | |_) \___ \| |_| || ||  \| |  _|  ##
##| |__| |_| |  _ < ___) |  _  || || |\  | |___ ##
## \____\___/|_| \_\____/|_| |_|___|_| \_|_____|##
##################################################

#Usage: python3 portscannercorshine.py (ip)


import nmap 

import sys 
target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]
scan_v = nmap.PortScanner()
print("\nScanning",target,"for ports 21,22,80,139,443 and 8080...\n")
for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port," is ",portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state']) 
print("\nHost",target," is ",portscan['scan'][list(portscan['scan'])[0]]['status']['state'])
