import cv2
...
cam = cv2.VideoCapture(0)

if cam.isOpened():
    print("Camera successfully opened")
else:
    print("Camera could not be opened")

while True:
    success, image = cam.read() 
    print("success in taking image? ", success)
    if success and not image.empty():
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        // further code to be excecuted to process the image
    else:
        print("problem capturing image")