def create_hostapd(iface, essid, channel):
    iface_str= "interface="+str(iface)+"\n"
    body_str= "driver=nl80211\n"
    body_str+= "ssid="+str(essid)+"1\n"
    body_str+= "hw_mode=g\n"
    body_str+= "channel=11\n"
    body_str+= "macaddr_acl=0\n"
    body_str+= "ignore_broadcast_ssid=0\n"
    conf_str= iface_str+body_str
    f = open("hostapd.conf", "w+")
    f.write(conf_str)
    #os.chmod("hostapd.conf",0o777)

def create_dnsmasq(iface):
    iface_str= "interface="+str(iface)+""
    body_str= "\ndhcp-range=192.168.2.2,192.168.2.230,255.255.255.0,12h"
    body_str+="\ndhcp-option=3,192.168.2.1"
    body_str+="\ndhcp-option=6,192.168.2.1"
    body_str+="\nserver=8.8.8.8"
    body_str+="\nserver=8.8.4.4"
    body_str+="\nlog-queries"
    body_str+="\nlog-dhcp"
    body_str+="\nlisten-address=127.0.0.1"
    body_str+="\nlisten-address=192.168.2.1"
    conf_str = iface_str+body_str
    f = open("dnsmasq.conf", "w+")
    f.write(conf_str)
    #os.chmod("dnsmasq.conf",0o777)

def create_dhcpd(essid):
    body_str = "\nauthoritative;"
    body_str += '\ndefault-lease-time 600;'
    body_str += '\nmax-lease-time 7200;'
    body_str += '\nsubnet 192.168.2.0 netmask 255.255.255.0 {'
    body_str += '\noption routers 192.168.2.1;'
    body_str += '\noption subnet-mask 255.255.255.0;'
    #body_str += '\noption domain-name '+str(essid)+';'
    body_str += '\noption domain-name test;'
    body_str += '\noption domain-name-servers 192.168.2.1;'
    body_str += '\nrange 192.168.2.2 192.168.2.40;'
    body_str += '\n}' 
    f = open("dhcpd.conf", "w+")
    f.write(body_str)