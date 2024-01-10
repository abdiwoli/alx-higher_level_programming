#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach(a => {
    if (a === searchElement) {
      n++;
    }
  });
  return n;
};
