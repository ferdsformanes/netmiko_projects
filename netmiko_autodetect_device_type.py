from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect

# Device info (without device_type)
device_info = {
    "host": "sbx-nxos-mgmt.cisco.com",
    "device_type": "autodetect",
    "username": "admin",     
    "password": "Admin_1234!",    
}

# Create SSHDetect object
guesser = SSHDetect(**device_info)

# Try to auto-detect the device type
best_match = guesser.autodetect()
if best_match:
    print(f"Detected device type: {best_match}")
    # Now create a Netmiko connection using the detected type
    device_info["device_type"] = best_match
    with ConnectHandler(**device_info) as connection:
        connection.find_prompt()
        print(connection.find_prompt())
else:
    print("Could not detect device type.")


# References:
# https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md#auto-detection-using-ssh