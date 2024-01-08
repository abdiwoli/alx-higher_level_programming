#!/usr/bin/node
const arg = process.argv;
const len = arg.length;
if (len === 2) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
