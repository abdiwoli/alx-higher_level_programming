#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
require('request')(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const responseBody = JSON.parse(response.body);
    console.log(responseBody.title);
  }
});
