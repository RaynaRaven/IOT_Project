import cv2
from pyzbar.pyzbar import decode
from sense_hat import SenseHat
import time
from datetime import datetime
import requests

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

# Create funtion to decode the barcode from input image 
# and query database to get product name
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
       
        # loop through the detected barcodes in image
        for barcode in detectedBarcodes: 

            #visual test for barcode reader, places bounding box and
            #text on barcode image, and displays the image.
            # Locate the barcode position in image
            #(x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            # cv2.rectangle(img, (x-10, y-10),
                          #(x + w+10, y + h+10),
                          #(255, 0, 0), 2) 

            #if barcode.data!="":
                #Display the image on display :1
                #cv2.imshow("Image", img)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()

            barcode = barcode.data.decode()
            if barcode.isnumeric():  
            # Print the barcode data
                print(barcode)
                url = f"https://world.openfoodfacts.org/api/v2/search?code={barcode}&fields=brands_tags,product_name"
                
                response = requests.get(url)

                #print(response.status_code)
                if response.status_code == 200:
                  data = response.json()
                  print(data)

                  # Extract the brands and product name from the data dictionary
                  brand = data['products'][0]['brands_tags'][0]
                  product_name = data['products'][0]['product_name']
                
                # Concat brand and product name into a single string using string literal formatting
                  product = f"{brand} {product_name}"
                  #print(product)
                  
                  #Get the current date and format it as a string
                  #now = datetime.now().strftime("%Y-%m-%d")

                  # Create dict with the product name, date, and date added
                  product_data = {
                  "product_name": product,
                  "expiry_date": None
                  }

                  #green light to signal barcode detected successfully
                  sense.set_pixels(patternT)
                  time.sleep(2)
                  sense.clear(O)

                  #print(product_data)
                  return product_data


                #TODO
                # else: email to user "Dear User, a barcode you recently added was not found on Open Food Facts Database. 
                # Please login to your app to enter it manually or contributing item details to the Open Food Facts Database here: <hyperlink> "

                

if __name__ == "__main__":
  # Take the image from user
  #image='images/Blank.jpg'# blank jpg for test purposes
  image="images/barcodes/test2.jpg" 
  BarcodeReader(image)