#!/usr/bin/node
const arg = process.argv[2];

if (arg && is NaN(arg) === false) {
  const arg2int = parseint(arg);
  console.log('My number:' + arg2int);
} else {
  console.log('Not a number')
}
