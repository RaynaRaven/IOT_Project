# Importing library
import cv2
from pyzbar.pyzbar import decode
from sense_hat import SenseHat
import time

sense = SenseHat()
red = (255,0,0)
green= (0,255,0)
X = (red)
T=(green)
O = (0,0,0)
patternX= [
  O,O,O,O,O,O,O,O,
  O,X,O,O,O,O,X,O,
  O,O,X,O,O,X,O,O,
  O,O,O,X,X,O,O,O,
  O,O,O,X,X,O,O,O,
  O,O,X,O,O,X,O,O,
  O,X,O,O,O,O,X,O,
  O,O,O,O,O,O,O,O
]

patternT= [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,T,T,
  O,O,O,O,O,T,T,O,
  O,O,O,O,T,T,O,O,
  T,T,O,T,T,O,O,O,
  O,T,T,T,O,O,O,O,
  O,O,T,O,O,O,O,O,
  O,O,O,O,O,O,O,O
]

#clear sensehat and init light_state
sense.clear()

# Make one method to decode the barcode
def BarcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
        sense.set_pixels(patternX)
        time.sleep(2)
        sense.clear(O)
    else:
       
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)
            #green light to signal barcode detected successfully
                sense.set_pixels(patternT)
                time.sleep(2)
                sense.clear(O)

    # Saving the image for test purposes
    cv2.imwrite("bc.jpg", img)
                 
    #Display the image on display :1
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
  # Take the image from user
    image="glensallaghTurkey.png" #"Blank.jpg" (for test purposes)
    BarcodeReader(image)