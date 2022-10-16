function toHex(numb){
    let tempnum = numb
    if (tempnum < 0){
        tempnum = 0;
    }
    else if (tempnum > 255){
        tempnum = 255;
    }
    tempnum = tempnum.toString(16)
    if (tempnum.length < 2){
        tempnum = "0" + tempnum
    }
    return tempnum.toUpperCase()
}
function rgb(r, g, b){
    return toHex(r) + toHex(g) + toHex(b)
  }
console.log(rgb(0,0,-20))



