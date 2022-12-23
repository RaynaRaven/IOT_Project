"use strict";

const firebase=require('firebase')
const firebaseConfig = {
    apiKey: "AIzaSyA_F-aiZOwe6YFSx9RRw7VVZ7uit3T1ZJc",
    authDomain: "foodsaveriot.firebaseapp.com",
    databaseURL: "https://foodsaveriot-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "foodsaveriot",
    storageBucket: "foodsaveriot.appspot.com",
    messagingSenderId: "142911850749",
    appId: "1:142911850749:web:6e21c26cbf692862589694",
    measurementId: "G-SMBKHBT2TX"
  };

firebase.initializeApp(firebaseConfig);
// Initialize Realtime Database and get a reference to the service
const db=firebase.database();
const Items=db.ref("Items");

module.exports = Items;