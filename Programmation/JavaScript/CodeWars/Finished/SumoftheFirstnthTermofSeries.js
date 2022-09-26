function SeriesSum(n){
    console.log("n is equal to : ",n)
    var sum = 1;
    if (n === 0 || n === Infinity || n === 1) {
      return "1.00"
    } 
    else {
      for (let i = 0; i < n-1; i++){
      sum += (1 / ((i*3) + 4))
      console.log("sum inside for loop", sum)
      }
    }
    console.log("sum before rounding up : ",sum)
    
    return (sum.toFixed(2)).toString()
  }
console.log(SeriesSum(1))
console.log(SeriesSum(2))
console.log(SeriesSum(3))
console.log(SeriesSum(4))
console.log(SeriesSum(144))