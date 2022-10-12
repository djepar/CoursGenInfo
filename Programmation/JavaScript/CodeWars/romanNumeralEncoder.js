//Create a function taking a positive integer as its parameter and
// returning a string containing the Roman Numeral representation of that integer.



let dicSym = {
  "M": 1000,
  "D": 500,
  "C": 100,
  "L": 50,
  "X": 10,
  "V": 5,
  "I": 1,
}



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
function nextSymbol(num, symArrays){
  for (el in dicSym){
    console.log(el)
    if (dicSym[el] <= num){
      if (!(MoreThree(symArrays, el))){
        return el
      }
    }
  }
}

// console.log(nextSymbol(symbols, 1050, ["M", "M", "M"]))
console.log(nextSymbol(1663, []))
function solution(number){
  let currentValue = number;
  let symArrays = [];
  // while (currentValue !== 0){
  //   let tempSym = nextSymbol(currentValue, symArrays);
  //   console.log(tempSym)
  //   currentValue -= symbols[]
  // }
}


