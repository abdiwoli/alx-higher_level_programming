#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
require('request')(url, function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body).characters;
    slowPrint(result, 0);
  }
});

function slowPrint (characters, index) {
  require('request')(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        slowPrint(characters, index + 1);
      }
    }
  });
}
