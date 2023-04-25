#!/usr/bin/node
// A script that reads and prints the content of a file

const file = process.argv[2];
const fs = require('fs');

fs.readFil0-readme.jse(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
