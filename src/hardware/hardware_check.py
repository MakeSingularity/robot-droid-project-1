import cv2
import subprocess

def check_cameras():
    # Check for camera 0
    cap0 = cv2.VideoCapture(0)
    if not cap0.isOpened():
        print("Camera 0 not detected.")
    else:
        print("Camera 0 is detected.")
        cap0.release()

    # Check for camera 1
    cap1 = cv2.VideoCapture(1)
    if not cap1.isOpened():
        print("Camera 1 not detected.")
    else:
        print("Camera 1 is detected.")
        cap1.release()

def check_ai_hat():
    # Check for AI HAT (assuming it's the Hailo AI HAT)
    result = subprocess.run(['lsusb'], stdout=subprocess.PIPE)
    if 'Hailo' in result.stdout.decode():
        print("AI HAT (Hailo AI HAT) is detected.")
    else:
        print("AI HAT (Hailo AI HAT) not detected.")

if __name__ == "__main__":
    print("Checking hardware...")
    check_cameras()
    check_ai_hat()