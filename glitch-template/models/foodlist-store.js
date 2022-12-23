'use strict';

const logger = require('../utils/logger');
const ListCollection = require('./foodlist-store.js');

const foodList = {
    index(request, response) {
        const viewData = {
            title: 'foodList',
        };
        response.render('foodList', viewData);
    },
};

module.exports = ListCollection;