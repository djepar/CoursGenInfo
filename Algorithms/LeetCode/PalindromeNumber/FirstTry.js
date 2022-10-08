/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let xString = x.toString();
    xString = xString.split("");
    //console.log(xString)
    for (let i = 0; i < xString.length; i++){
        let negIndex = (xString.length - (i+1))
        if (xString[i] !== xString[negIndex]){
            return false
            //console.log(xString[i], xString[negIndex])
        }
    }
    return true
};


console.log(isPalindrome(12345))
console.log(isPalindrome(2222))