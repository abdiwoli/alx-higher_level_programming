#!/usr/bin/node
const arg = process.argv.slice(2);
if (!isNaN(arg[0])) {
  let n = parseInt(arg[0]);
  while (n > 0) {
    console.log('C is fun');
    n--;
  }
} else {
  console.log('Missing number of occurrences');
}
