const fs = require('fs');

let input = fs.readFileSync('/dev/stdin', 'utf8').trim()
let money = 1000 - parseInt(input);

let coins = [500,100,50,10,5,1];

let count = 0;
for (let coin of coins) {
    count += Math.floor(money/coin)
    money %= coin;
}

console.log(count);