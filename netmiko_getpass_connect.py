from netmiko import ConnectHandler
from getpass import getpass

# Prompt for username and password securely
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Device details
device = {
    "device_type": "cisco_ios",  # Replace with your device type
    "host": "your_device_ip",
    "username": username,
    "password": password,
}

# Establish Netmiko connection
try:
    net_connect = ConnectHandler(**device)
    print("Connected successfully!")

    # Example: Send a command
    output = net_connect.send_command("show version", use_textfsm=True)
    print(output)

    net_connect.disconnect()
except Exception as e:
    print(f"Error connecting: {e}")