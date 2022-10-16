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
};
let listSym = ["M", "D", "C", "L", "X", "V","I"];

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
  for (let i = 0; i < listSym.length; i++){
    if (dicSym[listSym[i]] <= num){
      //if (!(MoreThree(symArrays, listSym[i]))){
      if (symArrays[symArrays.length -1] === symArrays[symArrays.length  -2] &  symArrays[symArrays.length  -2] === symArrays[symArrays.length  -3]){
        if ((dicSym[listSym[i]] + dicSym[listSym[i-1]])  <= num){
          let newlist = symArrays;
          newlist.pop;
          newlist.pop;
          newlist.pop;
          newlist.push(listSym[i-1]);
          newlist.push(listSym[i])
          return newlist
        }
        return listSym[i]
      }
    }
  }
}

console.log(nextSymbol(1050, ["M", "M", "M"]))
console.log(nextSymbol(4, ["I", "I", "I"]))

//console.log(nextSymbol(1663, []))
function solution(number){
  let currentValue = number;
  let symArrays = [];
  while (currentValue !== 0){
    let tempSym = nextSymbol(currentValue, symArrays);
    console.log(tempSym)
    currentValue -= dicSym[tempSym]
    symArrays.push(tempSym)
    console.log(currentValue)

  }
  return symArrays
}
//console.log(solution(99))


