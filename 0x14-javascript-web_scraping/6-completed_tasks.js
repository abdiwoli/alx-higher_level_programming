#!/usr/bin/node
const url = process.argv[2];
require('request')(url, (err, response, body) => {
  if (!err) {
    const jsonify = JSON.parse(body);
    const tasks = {};
    jsonify.forEach((task) => {
      if (task.completed && task.userId) {
        tasks[task.userId] = (tasks[task.userId] || 0) + 1;
      }
    });
    console.log(tasks);
  }
});
