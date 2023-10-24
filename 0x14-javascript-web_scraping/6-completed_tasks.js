#!/usr/bin/node

const request = require('request');

request((process.argv[2]), function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    for (const i in (JSON.parse(body))) {
      const tasks = (JSON.parse(body))[i];
      if (tasks.completed === true) {
        if (completed[tasks.userId] === undefined) {
          completed[tasks.userId] = 1;
        } else {
          completed[tasks.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
