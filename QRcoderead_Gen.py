import pyqrcode
import cv2
import os

def code_gen():
    print("\n===== QR Code Generator =====")
    print("Welcome to QR Code Generator App")
    msg = input("Enter Your Secret Message: ")
    file_name = input("Enter a File Name (without extension)")
    img  = pyqrcode.create(msg)
    img.png(f"{file_name}.png", scale=5)
    print(f"QR Code Generated Successfully! Saved as {file_name}.png")
    
def code_read():
    print("\n===== QR Code Reader =====")
    fileName = input("Enter QR image file name (with .png): ")
    if not (fileName.endswith(".png")):
        fileName = fileName + ".png"
    if not os.path.exists(fileName):
        print(" File not found!")
        return 
    img = cv2.imread(fileName)
    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)
    if data:
        print("\nYour Secret Message is:")
        print(data)
    else:
        print("QR Code detected, but unable to decode data!")


print("=== Welcome to QR Code App ===")
print("1. Generate QR Code")
print("2. Read QR Code")

choice = input("Enter Your Choice (1 or 2): ")

if choice == "1":
    code_gen()
elif choice == "2":
    code_read()
else:
    print("Invalid Choice! Please choose 1 or 2.")