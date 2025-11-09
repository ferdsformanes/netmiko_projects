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

# list to store all results
all_outputs = []

# simple for loop
for dev in devices:
    conn = ConnectHandler(**dev)  # connect to device
    output = conn.send_command("show inventory", use_textfsm=True)  # parse command output
    conn.disconnect()  # always disconnect after use
    
    # Add device hostname and inventory data
    for item in output:
        item["device"] = dev["host"]
        all_outputs.append(item)

# convert to DataFrame and save
df = pd.DataFrame(all_outputs)
print(df)
df.to_excel("network_inventory.xlsx", index=False)
