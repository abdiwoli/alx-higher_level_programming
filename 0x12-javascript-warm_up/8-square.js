#!/usr/bin/node
const arg = process.argv.slice(2);
if (!isNaN(arg[0])) {
  let n = parseInt(arg[0]);
  const nn = n;
  while (n > 0) {
    console.log('X'.repeat(nn));
    n--;
  }
} else {
  console.log('Missing size');
}
