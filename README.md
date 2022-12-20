# Food Saver 
#### Student Name: Carol Marjara   Student ID: 20099905

![alt text](https://github.com/RaynaRaven/IOT_Project/blob/main/reduceFoodWaste.png?raw=true)

FoodSaverIOT is a web application that helps users reduce food waste by providing reminders to use up items before they expire. 

It is designed to work with an Internet of Things (IoT) device with a connected camera module, which captures information from images of grocery shopping and sends notifications to the user to encourage them to use or freeze perishable items before they expire. By utilizing this technology, FoodSaverIOT aims to help users make the most of their food purchases and reduce waste.

It works by scanning food barcodes and expiry dates and storing this information in a database. The system uses a Raspberry Pi camera module and several libraries, including CV2, numpy, pyzbar, and tesseract OCR, to capture and read the barcodes and expiry dates. The LED matrix on the raspberry pi SenseHAT is utilised to signal to the user that images have been read successfully. It also queries a food database API, Open Food Facts, to retrieve the product name. If the barcode is not found in the database, the user is invited via email to contribute the missing information to the Open Food Facts API.

The scanned data is then sent to a Firebase real-time database, which serves as persistent storage for a web application created using Glitch, node.js and express framework. The user can log in to this app to view, update, and delete their list of scanned food items. If an item is about to expire, A red LED alert is displayed on the Sense HAT LED matrix until the user removes the expiring item from their list. The system also sends email reminders to the user 48 hours prior to the expiry date of a particular item, to remind them to use or freeze it before it goes bad.


## Tools, Technologies and Equipment

- Raspberry Pi 4, Sense HAT & Camera Module
- Glitch (JavaScript/Node/Express)
- Visual Studio Code
- Python 3.9
- Firebase
- HTTP

## Project Repository
https://github.com/RaynaRaven/IOT_Project
