#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const values = Object.values(dict);

values.forEach(v => {
  newDict[v] = Object.keys(dict).filter(key => dict[key] === v);
});

console.log(newDict);
