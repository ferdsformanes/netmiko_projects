from netmiko import ConnectHandler
import pandas as pd              

# define two devices
devices = [
    {
        "device_type": "cisco_nxos",
        "host": "sbx-nxos-mgmt.cisco.com",
        "username": "admin",
        "password": "Admin_1234!",
    },
    {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
    },
]



# simple for loop
for dev in devices:
    conn = ConnectHandler(**dev)
    output = conn.send_command("show inventory", use_textfsm=True)

# convert to DataFrame and save
df = pd.DataFrame(output)
print(df.to_string())
df.to_excel("network_inventory.xlsx", index=False)
