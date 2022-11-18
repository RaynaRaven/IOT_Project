# Food Saver 
#### Student Name: Carol Marjara   Student ID: 20099905


![alt text](https://github.com/RaynaRaven/IOT_Project/blob/main/reduceFoodWaste.png?raw=true)


The food saver system is a product scanner and notification system that helps to reduce food waste by scanning food barcodes and expiry dates, storing this information in a database and reminding the user via email 48 hours prior to the expiry date that the particular item will expire soon. 

Raspberry Pi camera module will capture barcode and expirydate from products (using CV2, numpy, pyzbar and tesseract OCR libraries) and a green tick LED will acknowledge data from image has been read. 

Data is sent to a web app which queries a food db and stores the retrieved product information and expiry date in a new user table. If the barcode is missing from database, user will be invited to contribute to the Open Food Facts DB (*see https://world.openfoodfacts.org/*)

When user consumes their food item they can log in to the app and remove the item from their food list

If the item is not removed from the users food list 48 hours prior to the expiry date, a red LED alert will be displayed on the sense HAT led array and an email reminder or push notification will be sent to the user to remind them to use or freeze that particular item.

## Tools, Technologies and Equipment

- Raspberry Pi 4, Sense HAT & Camera Module
- Glitch (Node/Express)
- Visual Studio Code
- Python 3.11
- SQL
- Javascript
- UDP
- HTTP
- TCP

## Project Repository
https://github.com/RaynaRaven/IOT_Project
