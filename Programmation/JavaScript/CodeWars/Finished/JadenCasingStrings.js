String.prototype.toJadenCase = function () {
    let newString = this.split(" ");
    let newNewString = ""
    for(el of newString){
       newNewString += el[0].toUpperCase() + el.substring(1,) + " ";
    }
    console.log(newNewString)
    return newNewString.substring(0,newNewString.length-1);
};

var str = "How can mirrors be real if our eyes aren't real"
console.log(str.toJadenCase())