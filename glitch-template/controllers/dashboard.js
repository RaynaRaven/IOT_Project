"use strict";

const logger = require("../utils/logger");
const listCollection = require("../models/foodlist-store.js")

const dashboard = {
  index(request, response) {
    logger.info("dashboard rendering");
    const viewData = {
      title: "Food Saver Dashboard",
      listCollection: listCollection
    };
    logger.info('about to render', listCollection)
    response.render("dashboard", viewData);
  },
};

module.exports = dashboard;
