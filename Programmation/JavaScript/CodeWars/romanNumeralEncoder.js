//Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

let symbols = [
  { "sym" : "M",
    "value": 1000 },
    { "sym" : "D",
    "value": 500 },
    { "sym" : "C",
    "value": 100 },
    { "sym" : "L",
    "value": 50 },
    { "sym" : "X",
    "value": 10 },
    { "sym" : "V",
    "value": 5 },
    { "sym" : "I",
    "value": 1 }

]
//console.log(symbols)


//Pass the array to see if there is less than 3 consecutive symbols
function MoreThree(arrayNum, target){
  if (arrayNum[arrayNum.length -1] === arrayNum[arrayNum.length  -2] &  arrayNum[arrayNum.length  -2] === arrayNum[arrayNum.length  -3]){
    if(arrayNum[arrayNum.length -1] === target){
      return true
    }
  }
  else {
    return false
  }
}
const test1 = ["M", "M", "M"]
const test2 = ["C"]
// console.log(MoreThree(test1));
// console.log(MoreThree(test2));
function nextSymbol(symbols, num, symArrays){
  for (el of symbols){
    console.log(el)
    if (el.value <= num){
      if (!(MoreThree(symArrays, el.sym))){
        return el.sym
      }
    }
  }
}

// console.log(nextSymbol(symbols, 1050, ["M", "M", "M"]))
console.log(nextSymbol(symbols, 1663, []))
function solution(number){
    // convert the number to a roman numeral
  }


