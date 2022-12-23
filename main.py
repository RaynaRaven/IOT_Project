from datetime import datetime
import barcode_scanner
import date_reader
import storeFileFB


def main():

    image="images/barcodes/test2.jpg" 

    #declare variable product_data to hold dect returned from barcodeReader()
    product_data=barcode_scanner.BarcodeReader(image)

    #assign date returned from dateReader to expiry date field
    product_data['expiry_date']=date_reader.dateReader()

    #get the current date
    dt = datetime.now()

    #format current date dt
    timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')

    #add new field and formatted date string to product_data
    product_data.update({'timestamp': timestamp })
    #print(product_data)

    #convert product data to json and push to rtdb
    storeFileFB.store_json(product_data)


if __name__ == "__main__":
    main()