#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
