from netmiko import ConnectHandler

# NX-OS device details
nxos = {
    "device_type": "cisco_nxos",
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
}

# IOS-XR device details
iosxr = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
}

def show_version(device):
    conn = ConnectHandler(**device)
    output = conn.send_command("show version")
    conn.disconnect()
    return output

# NX-OS
print("NX-OS Device Version Info:")
print(show_version(nxos))

# IOS-XR
print("\nIOS-XR Device Version Info:")
print(show_version(iosxr))
