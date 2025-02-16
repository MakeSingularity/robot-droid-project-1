#!/bin/bash

# Define variables
PI_USER=pi
PI_HOST=raspberrypi.local
PI_PATH=/home/pi/robot-droid-project

# Sync project files to Raspberry Pi
rsync -avz --exclude 'venv' --exclude '.git' --exclude '__pycache__' . $PI_USER@$PI_HOST:$PI_PATH

# SSH into Raspberry Pi and install dependencies
ssh $PI_USER@$PI_HOST << 'ENDSSH'
cd /home/pi/robot-droid-project
sudo apt-get update
sudo apt-get install -y python3-gi
pip install -r requirements.txt
ENDSSH

echo "Project files updated and dependencies installed on Raspberry Pi."