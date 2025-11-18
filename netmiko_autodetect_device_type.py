from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect

# Device with device_type set to autodetect
device = {
    "host": "sbx-nxos-mgmt.cisco.com",
    "device_type": "autodetect",
    "username": "admin",     
    "password": "Admin_1234!",    
}

# Create SSHDetect object
guesser = SSHDetect(**device)
best_match = guesser.autodetect()

# If auto-detection returned a valid device type, run the block below
if best_match:
    print(f"Detected device type: {best_match}")
    # Update the 'device' dictionary with the device_type
    device["device_type"] = best_match

    with ConnectHandler(**device) as connection:
        print(connection.find_prompt())
else:
    print("Could not detect device type.")


# References:
# https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md#auto-detection-using-ssh
