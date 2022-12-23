"use strict";

const express = require("express");
const router = express.Router();
const foodList = require('./controllers/foodList.js')

const dashboard = require("./controllers/dashboard.js");
const about = require("./controllers/about.js");

router.get("/", dashboard.index);
router.get("/dashboard", dashboard.index);
router.get("/about", about.index);
router.get('/foodList/:id', foodList.index)

module.exports = router;
