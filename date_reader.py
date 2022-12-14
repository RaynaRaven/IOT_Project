import cv2
import pytesseract
import numpy as np
from pytesseract import Output
from sense_hat import SenseHat
import re
import calendar
from datetime import datetime
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

MM_YY = r'\d{2}/\d{4}'
DD_MM_YY = r'\d{2}/\d{2}/\d{2}'
DD_MM_YYYY = r'\d{2}/\d{2}/\d{4}'
DD_Month = re.compile((r'\b\d{2} [A-Z]{3}\b'))

fileLoc= 'images/dates/test2z.jpg'

def dateReader():

    #TODO prepare camera to scan image
    #camera module not currently working, arducam libcamera autofocus option causing segmentation error
    #no reply from Arducam support as of 23/12/22

    #initialise sensehat and display ready message on LED matrix
    sense = SenseHat()
    blue = (0,0,255)
    #prompt user to scan image when camera is ready
    #sense.show_message("ready, scan date", text_colour=blue, scroll_speed=0.05)

    # loading test image, camera currently not working
    img_source = cv2.imread(fileLoc)

    #preprocessing functions to convert to gray values using cv2
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
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(d['text'])
        
        # back to RGB
        #if len(img.shape) == 2:
        #    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        
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

    #uncomment to check output dict
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
    print("match found: ", date)

    # Parse the input date string and convert it to a datetime object
    date_time = datetime.strptime(date, "%m/%Y")

    # Get the number of days in the month of the datetime object
    _, num_days = calendar.monthrange(date_time.year, date_time.month)

    # Set the day to the last day of the month and the month to the month of the datetime object
    last_day_of_month = date_time.replace(day=num_days, month=date_time.month)

    # Convert the updated datetime object to a string in the desired format
    formatted_date = last_day_of_month.strftime("%Y-%m-%d")
    print("success!", formatted_date)  # prints "2023-06-30""30-06-2023"
    #green light to signal barcode detected successfully
    sense.set_pixels(patternT)
    time.sleep(2)
    sense.clear(O)

    return formatted_date

    #TODO write functions to handle other date patterns identified

if __name__ == "__main__":
    dateReader()