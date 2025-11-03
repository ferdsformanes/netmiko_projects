from netmiko import ConnectHandler

# dictionary (key:value pairs) with device details
device = {
    "device_type": "cisco_nxos",    
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

# create SSH connection object (** unpacks dictionary into arguments)
connection = ConnectHandler(**device)

# run command by calling send_command() with a string 
output = connection.send_command("show version")
print(output)  # print command output

connection.disconnect()  # close connection
