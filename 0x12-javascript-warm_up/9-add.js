#!/usr/bin/node
const arg = process.argv.slice(2);
if (!isNaN(arg[0]) && !isNaN(arg[1])) {
  const n1 = parseInt(arg[0]);
  const n2 = parseInt(arg[1]);
  add(n1, n2);
} else {
  console.log('NaN');
}

function add (a, b) {
  console.log(a + b);
}
