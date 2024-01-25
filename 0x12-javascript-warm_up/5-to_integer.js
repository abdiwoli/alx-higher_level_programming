#!/usr/bin/node
<<<<<<< HEAD
const arg = process.argv;
if (arg[3]) {
  console.log('My number: ' + arg[2]);
} else {
  console.log('No argument');
=======
const arg = process.argv.slice(2);
if (!isNaN(arg[0])) {
  console.log('My number: ' + arg[0]);
} else {
  console.log('Not a number');
>>>>>>> 86d67e17d723a3dac9a7161b1808316f4b36bd59
}
