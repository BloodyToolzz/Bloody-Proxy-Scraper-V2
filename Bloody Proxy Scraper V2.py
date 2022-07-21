import os, time, requests, pystyle, random, datetime

from pystyle import *
from console.utils import set_title

def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

h_h2 = ["Halal", "Haram"]

now = datetime.datetime.now()

cls()
os.system('mode 85, 25')
banner = '''
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗     
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝     
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝      
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝       
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║        
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝        
                                                        
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗              
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝              
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝               
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝                
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║                 
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝                 
                                                        
███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
A simple proxy scraper made by Bloody.
github/BloodyToolzz
'''
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
Write.Print("This program is: ", Colors.purple_to_blue, interval=0)
Write.Print(f"{random.choice(h_h2)}\n", Colors.green_to_white, interval=0)
Write.Print("Started at: " + now.strftime("%Y/%m/%d %H:%M:%S\n"), Colors.purple_to_blue , interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Scraping Proxies . . .")
Write.Print("\n[?] Scraping Proxies . . .\n", Colors.red_to_yellow, interval=0)

http = open('http.txt','wb')
socks4 = open('socks4.txt','wb')
socks5 = open('socks5.txt','wb')
allp = open('all.txt','wb')

# HTTP Proxies Sources
h = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
h1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt")
h2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
h3 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt")
h4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt")
h5 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
h6 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt")
h7 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
h8 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
h9 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
h10 = requests.get("https://www.proxyscan.io/download?type=http")
h11 = requests.get("https://www.proxyscan.io/download?type=https")
h12 = requests.get("https://api.openproxylist.xyz/http.txt")

# SOCKS4 Proxies Sources
s4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt")
s41 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
s42 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt")
s43 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt")
s44 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt")
s45 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
s46 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
s47 = requests.get("https://www.proxyscan.io/download?type=socks4")
s48 = requests.get("https://api.openproxylist.xyz/socks4.txt")

# SOCKS5 Proxies Sources
s5 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt")
s51 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
s52 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt")
s53 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt")
s54 = requests.get("https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks5.txt")
s55 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt")
s56 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
s57 = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
s58 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
s59 = requests.get("https://www.proxyscan.io/download?type=socks5")
s510 = requests.get("https://api.openproxylist.xyz/socks5.txt")

# All Proxies Sources
all1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt")
all2 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies.txt")
all3 = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt")
all4 = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt")
all5 = requests.get("http://hack-hack.chat.ru/proxy/allproxy.txt")
all6 = requests.get("http://hack-hack.chat.ru/proxy/p1.txt")
all7 = requests.get("http://hack-hack.chat.ru/proxy/p2.txt")
all8 = requests.get("http://hack-hack.chat.ru/proxy/p3.txt")
all9 = requests.get("http://hack-hack.chat.ru/proxy/p4.txt")
all10 = requests.get("http://olaf4snow.com/public/proxy.txt")
all11 = requests.get("http://alexa.lr2b.com/proxylist.txt")
all12 = requests.get("http://inav.chat.ru/ftp/proxy.txt")

set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Finished Scraping Proxies!")
Write.Print(f"[!] Finished Scraping Proxies!\n", Colors.green_to_white, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Writing Proxies . . .")
Write.Print("[?] Writing Proxies In Files . . .\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing Proxies In Their Files
# Writing HTTP Proxies
http.write(h.content)
http.write(h1.content)
http.write(h2.content)
http.write(h3.content)
http.write(h4.content)
http.write(h5.content)
http.write(h6.content)
http.write(h7.content)
http.write(h8.content)
http.write(h9.content)
http.write(h10.content)
http.write(h11.content)
http.write(h12.content)

# Writing SOCKS4 Proxies
socks4.write(s4.content)
socks4.write(s41.content)
socks4.write(s42.content)
socks4.write(s43.content)
socks4.write(s44.content)
socks4.write(s45.content)
socks4.write(s46.content)
socks4.write(s47.content)
socks4.write(s48.content)

# Writing SOCKS5 Proxies
socks5.write(s5.content)
socks5.write(s51.content)
socks5.write(s52.content)
socks5.write(s53.content)
socks5.write(s54.content)
socks5.write(s55.content)
socks5.write(s56.content)
socks5.write(s57.content)
socks5.write(s58.content)
socks5.write(s59.content)
socks5.write(s510.content)

# Writing All Proxies 
allp.write(all1.content)
allp.write(all2.content)
allp.write(all3.content)
allp.write(all4.content)
allp.write(all5.content)
allp.write(all6.content)
allp.write(all7.content)
allp.write(all8.content)
allp.write(all9.content)
allp.write(all10.content)
allp.write(all11.content)
allp.write(all12.content)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Wrote Proxies!")
Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.green_to_white, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Closing Files . . .")
Write.Print("[?] Closing Files . . .\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Closing Files
http.close()
socks4.close()
socks5.close()
allp.close()

# Done!
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Finished!")
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.green_to_white, interval=0)
time.sleep(1)
Write.Print("Thanks for using my tools <3\n", Colors.red_to_yellow, interval=0.1)
Write.Print("Press any key to continue . . .", Colors.green_to_white, interval=0)
pause()
