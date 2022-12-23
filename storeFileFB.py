import firebase_admin
from firebase_admin import credentials, db
import os

# Load the service account key JSON file
cred=credentials.Certificate('./serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://foodsaveriot-626bc-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get a reference to the database root
ref = db.reference('/')

users = ref.child('users')

# Get a reference to the 'products' child node
products_ref = users.child('products')

def store_json(json_obj):
    # Update the 'products' node with the specified JSON object
    new_products_ref = products_ref.push(json_obj)
    product_id = new_products_ref.key
    print ("product added with uuid: ", product_id)

if __name__ == "__main__":
    # Store the JSON object in the Realtime Database
    store_json()