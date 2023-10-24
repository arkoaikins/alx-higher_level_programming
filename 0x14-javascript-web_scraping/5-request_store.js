#!/usr/bin/node
const url = process.argv[2];
const fs = require('fs');
const request = require('request');
request(url).pipe(fs.createWriteStream(process.argv[3]));
