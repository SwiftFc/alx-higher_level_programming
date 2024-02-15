#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);

if (!isNaN(firstArg)) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('Not a number');
}
