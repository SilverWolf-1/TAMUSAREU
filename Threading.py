import threading
import time
from PIL import Image
image = Image.open(r"C:\Users\J1016\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-03 204131.png")

def send():
    print("Look at what I sent you")
    time.sleep(1)
    image.show()

def recive():
    time.sleep(3)
    print("What did you send? nothing is showing up")
    time.sleep(4)
    print("Now I see it lol")

#Creating threads
threadA = threading.Thread(target=send)
threadB = threading.Thread(target=recive)

#Start
threadA.start()
threadB.start()

#Completion
threadA.join()
threadB.join()