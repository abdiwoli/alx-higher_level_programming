#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

require('request')(url, (err, response) => {
  if (!err) {
    const result = JSON.parse(response.body);
    result.characters.forEach((r) => {
      require('request')(r, (err, res) => {
        if (!err) {
          const body = JSON.parse(res.body);
          console.log(body.name);
        }
      });
    });
  }
});
