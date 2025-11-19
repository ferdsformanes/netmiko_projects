from netmiko import ConnectHandler

# Device inventory
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

# Target hostname to connect
target_host = "sandbox-iosxr-1.cisco.com"

# Use next() to find the first matching device
device = next((d for d in devices if d["host"] == target_host), None)

if device:
    print(f"Connecting to {device['host']}...")
    connection = ConnectHandler(**device)
    output = connection.send_command("show version")
    print("\nDevice Output:\n", output)
    connection.disconnect()
else:
    print("Device not found in inventory.")