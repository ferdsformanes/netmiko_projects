# Automate Cisco Device Inventory with Python (Netmiko + TextFSM + Pandas)

from netmiko import ConnectHandler
import pandas as pd

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

all_outputs = []

for dev in devices:  
    print(f"\n[OUTER LOOP] Connecting to {dev['host']}...")
    conn = ConnectHandler(**dev)
    output = conn.send_command("show inventory", use_textfsm=True)
    conn.disconnect()

    for item in output:
        print(type(item))
        print(f"   [INNER LOOP] Item: {item.get('name', 'unknown')} from {dev['host']}")
        item["device"] = dev["host"]
        all_outputs.append(item)

print(f"Total items collected: {len(all_outputs)}")
# convert to DataFrame and save
df = pd.DataFrame(all_outputs)
# print(df)
df.to_excel("device_inventory.xlsx", index=False)
