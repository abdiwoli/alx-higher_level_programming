#!/usr/bin/node
const url = process.argv[2];
require('request')(url, (err, response, body) => {
  if (!err) {
    require('fs').writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
