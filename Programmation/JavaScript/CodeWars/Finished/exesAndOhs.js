//Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

function XO(str){
    let exes = 0;
    let ohs = 0;
    for (letter of str){
        //console.log(letter)
        if (letter == 'x' || letter == 'X'){
            exes += 1;
        }
        else if (letter == 'o' || letter == 'O'){
            ohs += 1;
        }
    }
    //console.log(`exes = ${exes} ohs = ${ohs}`)
    return exes === ohs
}

console.log(XO("xxxm"))

//Best code on CodeWars
function XO(str) {
    let x = str.match(/x/gi);
    let o = str.match(/o/gi);
    return (x && x.length) === (o && o.length);
  }