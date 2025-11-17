from netmiko import ConnectHandler
from pwinput import pwinput
import pandas as pd


username = input("Enter your username: ")
# password = pwinput("Enter your password: ", mask='*')
password = pwinput.pwinput(prompt="Enter your password: ")
device = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": username,
    "password": password,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version", use_textfsm=True)

df = pd.DataFrame(output)
print(df)
df.to_excel("show_version.xlsx", index=False)

net_connect.disconnect()


# Reference: https://pypi.org/project/pwinput/

