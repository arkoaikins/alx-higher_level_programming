#!/usr/bin/node
// script that prints the first argument passed to it
const farg = process.argv[2];
if (farg) {
  console.log(farg);
} else {
  console.log('No argument');
}
