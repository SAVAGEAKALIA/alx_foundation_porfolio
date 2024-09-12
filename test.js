#!/usr/bin/env node
const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('What is your name?', (name) => {
    //name = this.getName(name);
    firstletter = name[0].toUpperCase()
    names = name.slice(1);
    named = firstletter + names
    console.log(named);
});

// const name = readline("What is your name");
// named = name.toUpperCase().slice(0,1)
// console.log(named)