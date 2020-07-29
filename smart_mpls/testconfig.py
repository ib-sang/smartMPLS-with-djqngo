from netmiko import Netmiko
import json
from napalm import get_network_driver
from netmiko import ConnectHandler

#driver = get_network_driver('ios')
#host='192.168.231.157'
#host='192.168.200.21'
#username='admin'
#password='admin'
#with driver(host, username, password, optional_args={}) as device:
#    output = device.get_interfaces()


config_commands=[]
params = {
        'ip': '192.168.200.21',
        'username': 'admin',
        'password' : 'admin',
        'device_type' : 'cisco_ios'
    }
command='show ip vrf interf'
#net_connect = Netmiko(**params)
#print(net_connect.find_prompt())
tab=[]
#with ConnectHandler(**params) as device_conf:
#    output = device_conf.send_command(command)

#output = output.split()  
  
#leng= len(output)
#i = 4
#print(leng)
js={}
j=0

#while i< leng:
    
#    js[output[i]] = {
#        "ip-address" : output[i+1],
#        "vrf" : output[i+2],
#        "protocol" : output[i+3]
#    }
    
#    i=i+4

#print(js)     
#while i< leng:
#    if output[i+1]=='<not':
#        js[j] = {
#        "name" : output[i],
#        "rd" : output[i+1] + ' ' + output[i+2],
#        "interface" : output[i+3],
#        }
#        i=i+4
#    else:
#        js[j] = {
#            "name" : output[i],
#            "rd" : output[i+1],
#            "interface" : output[i+2],
#        }
#        i=i+3
#    j=j+1



interf ={
    "PE1": {
        'Ethernet0/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:06', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 100}, 
        'GigabitEthernet0/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:08', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000}, 
        'GigabitEthernet1/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:1C', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet2/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:38', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet3/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:54', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet4/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:01:26:54:00:70', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet5/0': {'is_enabled': True, 'is_up': True, 'description': '', 'mac_address': 'CA:01:26:54:00:8C', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000}},
    "PE2": {
        'Ethernet0/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:06', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 100},
        'GigabitEthernet0/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:08', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet1/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:1C', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet2/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:38', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet3/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:54', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000}, 
        'GigabitEthernet4/0': {'is_enabled': False, 'is_up': False, 'description': '', 'mac_address': 'CA:02:05:0C:00:70', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000},
        'GigabitEthernet5/0': {'is_enabled': True, 'is_up': True, 'description': '', 'mac_address': 'CA:02:05:0C:00:8C', 'last_flapped': -1.0, 'mtu': 1500, 'speed': 1000}
        }
}

for device,devices in interf:
    print(device)
    for interface in devices:
        print(interface)