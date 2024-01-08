#!/usr/bin/node
const arg = process.argv.slice(2);
let len = arg.length;
const arr = Array(len);
if (len < 2) {
  console.log('0');
} else {
  arg.forEach(a => aray(a));
}
function aray (a) {
  len--;
  arr[len] = parseInt(a);
}
const mx = arr.indexOf(Math.max(...arr));
arr.splice(mx, 1);
console.log(Math.max(...arr));
