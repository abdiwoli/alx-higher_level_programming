#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

require('request')(url, (err, response) => {
  if (!err) {
    const result = JSON.parse(response.body).characters;
  }
});

