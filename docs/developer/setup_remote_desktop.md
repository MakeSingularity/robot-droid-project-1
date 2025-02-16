# Setting Up Remote Desktop Between Raspberry Pi 5 and Development Laptop

This document provides detailed instructions for developers on how to set up a remote desktop connection between the Raspberry Pi 5 running PIOS and the development laptop. 

## Prerequisites

1. **Hardware Requirements:**
   - Raspberry Pi 5 with PIOS installed.
   - Development laptop (Windows, macOS, or Linux).
   - HDMI cable (for initial setup if needed).
   - Network connection (Wi-Fi or Ethernet).

2. **Software Requirements:**
   - Remote Desktop Protocol (RDP) client installed on the development laptop.
   - SSH access to the Raspberry Pi (optional but recommended for troubleshooting).

## Installation Steps

### Step 1: Update Raspberry Pi

1. Connect to your Raspberry Pi via SSH or directly using a monitor and keyboard.
2. Open a terminal and run the following commands to update the system:

   ```
   sudo apt update
   sudo apt upgrade -y
   ```

### Step 2: Install xrdp

1. Install the xrdp package, which allows RDP connections:

   ```
   sudo apt install xrdp -y
   ```

2. Start the xrdp service:

   ```
   sudo systemctl enable xrdp
   sudo systemctl start xrdp
   ```

### Step 3: Configure xrdp

1. Ensure that the xrdp service is running:

   ```
   sudo systemctl status xrdp
   ```

2. If necessary, configure the firewall to allow RDP connections:

   ```
   sudo ufw allow 3389
   ```

### Step 4: Find Raspberry Pi IP Address

1. To connect to the Raspberry Pi, you need its IP address. Run the following command:

   ```
   hostname -I
   ```

2. Note down the IP address displayed.

### Step 5: Connect from Development Laptop

1. Open the RDP client on your development laptop.
2. Enter the Raspberry Pi's IP address and connect.
3. Log in using your Raspberry Pi credentials (default username is usually `pi`).

## Troubleshooting Tips

- **Connection Issues:** Ensure that both devices are on the same network and that the Raspberry Pi is powered on.
- **Firewall Settings:** Check the firewall settings on both the Raspberry Pi and the development laptop to ensure that RDP connections are allowed.
- **xrdp Service:** If you encounter issues, restart the xrdp service with:

  ```
  sudo systemctl restart xrdp
  ```

- **Check Logs:** Review the xrdp logs for any errors:

  ```
  cat /var/log/xrdp-sesman.log
  cat /var/log/xrdp.log
  ```

By following these steps, you should be able to successfully set up a remote desktop connection between your Raspberry Pi 5 and development laptop.