#!/usr/bin/node
const ls = require('./100-data').list;
console.log(ls);
const newlist = ls.map((el, idx) => el * idx);
console.log(newlist);
