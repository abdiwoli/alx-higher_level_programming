#!/usr/bin/node
require('https').get(process.argv[2], (response) => {
  console.log(`code: ${response.statusCode}`);
}).on('error', (error) => {
  console.error(`Error making GET request: ${error.message}`);
});
