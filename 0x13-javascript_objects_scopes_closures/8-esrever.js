#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  let n = list.length - 1;
  list.forEach(el => {
    arr[n] = el;
    n--;
  });
  return arr;
};
