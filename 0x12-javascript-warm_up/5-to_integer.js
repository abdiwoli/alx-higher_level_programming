#!/usr/bin/node
const arg = process.argv;
if (arg[3]) {
  console.log('My number: ' + arg[2]);
} else {
  console.log('No argument');
}
