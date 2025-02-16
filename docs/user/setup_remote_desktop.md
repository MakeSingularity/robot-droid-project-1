# Setting Up Remote Desktop for Raspberry Pi 5

This guide provides simplified instructions for end-users on how to establish a remote desktop connection with the Raspberry Pi 5 running PIOS. Follow these steps to get started.

## Prerequisites

1. **Raspberry Pi 5**: Ensure your Raspberry Pi 5 is powered on and running PIOS.
2. **Network Connection**: Both your Raspberry Pi and development laptop should be connected to the same network (Wi-Fi or Ethernet).
3. **Remote Desktop Software**: You will need a remote desktop client installed on your development laptop. Common options include:
   - **Windows**: Remote Desktop Connection
   - **macOS**: Microsoft Remote Desktop
   - **Linux**: Remmina or Vinagre

## Step-by-Step Instructions

### Step 1: Enable Remote Desktop on Raspberry Pi

1. Open a terminal on your Raspberry Pi.
2. Run the following command to install the XRDP server:
   ```
   sudo apt update
   sudo apt install xrdp
   ```
3. Once installed, start the XRDP service:
   ```
   sudo systemctl start xrdp
   ```
4. To ensure XRDP starts on boot, run:
   ```
   sudo systemctl enable xrdp
   ```

### Step 2: Find the Raspberry Pi's IP Address

1. In the terminal, run the following command to find your Raspberry Pi's IP address:
   ```
   hostname -I
   ```
2. Note down the IP address displayed (e.g., `192.168.1.10`).

### Step 3: Connect from Your Development Laptop

1. Open your remote desktop client on your development laptop.
2. Enter the Raspberry Pi's IP address in the connection field.
3. Click on "Connect" or "Start" to initiate the connection.
4. When prompted, enter your Raspberry Pi's username (default is `pi`) and password (default is `raspberry`).

### Step 4: Adjust Display Settings (Optional)

- If you experience display issues, you may need to adjust the resolution settings in your remote desktop client.

## Troubleshooting

- **Connection Issues**: Ensure both devices are on the same network and that the XRDP service is running on the Raspberry Pi.
- **Authentication Errors**: Double-check your username and password.
- **Performance Issues**: Consider lowering the resolution or color depth in your remote desktop client settings.

## Conclusion

You should now be able to access your Raspberry Pi 5 remotely from your development laptop. This setup will allow you to record demonstrations via HDMI0 and interact with your droid project effectively.