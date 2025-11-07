from netmiko import ConnectHandler  # import class from netmiko
import pandas as pd                 # import pandas as pd

# define connection parameters as a dictionary
device = {
    "device_type": "cisco_nxos",
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

# unpack dictionary into ConnectHandler arguments
connection = ConnectHandler(**device)

# run command with TextFSM parsing enabled
output = connection.send_command("show inventory", use_textfsm=True)

# convert list of dicts to DataFrame
frame = pd.DataFrame(output)

# write DataFrame to Excel file
frame.to_excel("nxos_inventory.xlsx", index=False)

# close SSH connection
connection.disconnect()

