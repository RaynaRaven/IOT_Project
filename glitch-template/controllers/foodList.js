'use strict';

const logger = require('../utils/logger');
const listCollection = require('../models/foodlist-store.js');

const foodList = {
    index(request, response) {
        const foodListId = request.params.id;
        logger.info('foodlist id: ' + foodListId);
        const viewData = {
            title: 'foodList',
        };
        response.render('foodList', viewData);
    },
};

module.exports = foodList;