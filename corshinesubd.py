##################################################
## / ___/ _ \|  _ \/ ___|| | | |_ _| \ | | ____|##
##| |  | | | | |_) \___ \| |_| || ||  \| |  _|  ##
##| |__| |_| |  _ < ___) |  _  || || |\  | |___ ##
## \____\___/|_| \_\____/|_| |_|___|_| \_|_____|##
##################################################

#Usage: python3 corshinesubd.py (domain)

import requests 
import sys 

sub_list = open("wordlistsubd.txt").read() 
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(url_to_check)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",url_to_check)
