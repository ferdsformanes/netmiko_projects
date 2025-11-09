from netmiko import ConnectHandler
import pandas as pd              

# define connection parameters as a dictionary
device = {
    "device_type": "cisco_nxos",
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

# unpack dictionary into ConnectHandler arguments
connection = ConnectHandler(**device)

# 'use_textfsm=True' converts raw CLI text into structured data (list of dicts)
output = connection.send_command("show inventory", use_textfsm=True)

# convert list of dicts to DataFrame
frame = pd.DataFrame(output)

# print full DataFrame without truncation
print(frame.to_string())

# write DataFrame to Excel file
frame.to_excel("nxos_inventory.xlsx", index=False)

# close SSH connection
connection.disconnect()



# References:
# https://pynet.twb-tech.com/blog/netmiko-and-textfsm.html
# https://github.com/networktocode/ntc-templates/blob/master/ntc_templates/templates/index
