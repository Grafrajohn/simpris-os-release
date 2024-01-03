"use strict";
/**
 * Created by Graham on 11/08/2016.
 */
// Simpris API tests
//
// Project
//
var user = 'testuser';
var password = 'past_password';
var url_base = 'http://127.0.0.1:8000';

console.log("--- api/project/list ---");

var page = require('webpage').create(),
    server = url_base,
    data = 'user=' + user + '&password=' + password;

page.open(server, 'get', data, function (status) {
    if (status !== 'success') {
        console.log('ERROR');
    }
    else {
        console.log('OK');
    }
    phantom.exit;
}

