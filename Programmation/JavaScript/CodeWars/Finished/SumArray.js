//Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
function sumArray(array) {
    if (array === null || array === NaN || array === undefined) {
      return 0;
    }
    else if (array.length <= 2 ){
      return 0;
    }
    else if (array.length == 2){
      return array[1]
    }
    newArray = array.sort(function(a,b){return a-b})
    let sum = 0;
    newArray.splice(-1, 1)
    newArray.splice(0,1);
    console.log(newArray)
     for (let e of newArray){
         console.log(e)
        sum += e;
    };
    return sum
  
  }


// the best solution I found on codewars : 
sumArray = a => a ? a.sort((x, y) => x - y).slice(1, -1).reduce((s, e) => s + e, 0) : 0
