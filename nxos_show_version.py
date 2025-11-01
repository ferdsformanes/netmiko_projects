from netmiko import ConnectHandler

# Device details (NX-OS)
device = {
    "device_type": "cisco_nxos",
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

# Connect to the device
connection = ConnectHandler(**device)

# Run "show version"
output = connection.send_command("show version")
print(output)

# Disconnect
connection.disconnect()
