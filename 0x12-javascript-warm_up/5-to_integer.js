#!/usr/bin/node
const arg = process.argv.slice(2);
if (!isNaN(arg[0])) {
  console.log('My number: ' + arg[0]);
} else {
  console.log('Not a number');
}
