# Food Saver 
#### Student Name: Carol Marjara   Student ID: 20099905

![alt text](https://github.com/RaynaRaven/IOT_Project/blob/main/reduceFoodWaste.png?raw=true)

The food saver system is a product scanner and notification system that helps to reduce food waste by scanning food barcodes and expiry dates, storing this information in a database and notifying the user via email 48 hours prior to the expiry date that the particular item will expire soon. An email reminder or push notification will be sent to the user to remind them to use or freeze that particular item.

Raspberry Pi camera module will capture barcode and expiry date from products (using CV2, numpy, pyzbar and tesseract OCR libraries) and a green tick LED will acknowledge data from the image has been read. The barcode is used to query a food database API e.g. Open food facts, and the product name is requested from the response.  If the barcode is missing from database, user will be invited to contribute to the Open Food Facts API (*see https://world.openfoodfacts.org/*)

The product data is sent from the raspberry to Firebase where it is stored in a realtime database which is connected to a Glitch app. The end user can login, view, update and delete their list of scanned food items e.g. when a user consumes their food item they can log in to the app and remove the item from their food list. A red LED alert will be displayed on the sense HAT led array until the user removes the expiring item from their food list.

## Tools, Technologies and Equipment

- Raspberry Pi 4, Sense HAT & Camera Module
- Glitch (Node/Express)
- Visual Studio Code
- Python 3.11
- Firebase
- Javascript
- HTTP
- TCP

## Project Repository
https://github.com/RaynaRaven/IOT_Project
