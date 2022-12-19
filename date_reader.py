import cv2
import pytesseract
import numpy as np
from pytesseract import Output
from sense_hat import SenseHat
import re
import calendar
from datetime import datetime

MM_YY = r'\d{2}/\d{4}'
DD_MM_YY = r'\d{2}/\d{2}/\d{2}'
DD_MM_YYYY = r'\d{2}/\d{2}/\d{4}'
DD_Month = re.compile((r'\b\d{2} [A-Z]{3}\b'))

#initialise sensehat and display ready image on LED matrix
sense = SenseHat()
blue = (0,0,255)
sense.show_message("Ready for next image, scan date", text_colour=blue, scroll_speed=0.05)

#loading test image, camera currently not working
img_source = cv2.imread('images/dates/test2z.jpg')

#TODO take image from live camera feed 

#preporcessing functions to convert to gray values using cv2
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
 
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
 
def canny(image):
    return cv2.Canny(image, 100, 200)
 
gray = get_grayscale(img_source)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

#initialise empty list for identified text
id_text = []

for img in [img_source, gray, thresh, opening, canny]:
    #d = pytesseract.image_to_data(img, output_type=Output.DICT)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
 
    # back to RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
 
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            # don't show empty text
            if text and text.strip() != "":
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img = cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                cv2.imwrite("/images/test_results/img"+str(i)+".jpg", img)
                #print(d)
                #print(text)
                for item in d['text']:
                    if item != '':
                        id_text.append(item)

#uncomment for output
#print(id_text)

def get_date(list):
    found_dates = set()
    for pattern in [MM_YY, DD_MM_YY, DD_MM_YYYY, DD_Month]:
        for item in list:
            match = re.match(pattern, item)
            if match and match.group() not in found_dates:
                found_dates.add(match.group())
                date = match.group()
                return date
                #print(f"{match.group()}")

#get date from id_text list, parse and convert to datetime object
date = get_date(id_text)
print(date)

# Parse the input date string and convert it to a datetime object
date_time = datetime.strptime(date, "%m/%Y")

# Get the number of days in the month of the datetime object
_, num_days = calendar.monthrange(date_time.year, date_time.month)

# Set the day to the last day of the month and the month to the month of the datetime object
last_day_of_month = date_time.replace(day=num_days, month=date_time.month)

# Convert the updated datetime object to a string in the desired format
formatted_date = last_day_of_month.strftime("%d-%m-%Y")
print(formatted_date)  # prints "30-06-2023"

#TODO write function for instance of date in format dd/mm/yyyy || dd/mm/yy

#cv2.imshow('img', img)
# #cv2.waitKey(0)