const binaryArrayToNumber = arr => {
    let total = 0;
    arr.reverse();
    for (let i = 0; i < arr.length; i++){
      if (arr[i] === 1){
        console.log(i,(2**i), total)
        total +=  (2**i)
      }
    }
    return total
  };

console.log(binaryArrayToNumber([1, 0, 1, 1]))

const binaryArrayToNumber2 = arr => {
    return parseInt(Number(arr.join('')),2)
}


console.log(binaryArrayToNumber2([1, 0, 1, 1]))
