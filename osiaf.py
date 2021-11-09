#!/usr/bin/python


# import some module

import requests
import os

os.system("clear")
os.system("cat banner")
user=str(input("\033[33musername / nametag :\033[0m "))
path_urls=open('url.txt', 'r')
link_urls=path_urls.readlines()
path_urls.close()

os.system("clear")
for url in link_urls:
    link=url.strip()
    check=link+user
    try:
        x=requests.get(check)
        if x.status_code == 200:
            print("\033[0;32maccount found : \033[0m"+check)
        else:
            print("\033[0;31maccount not found : \033[0m"+check)
    except requests.exceptions.MissingSchema:
        break

    except KeyboardInterrupt:
        print("\033[0;33m QUIT : KEYBOARD INTERRUPT")
        break
