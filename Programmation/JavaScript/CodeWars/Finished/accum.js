/*This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt" */


function accum(s){
    let newString = ""
    for (let i = 0; i < s.length; i++){
        let newPreString = s[i]
        for(let j = 0; j < i; j++){
            newPreString += s[i]
        }
        newPreString = newPreString.toLowerCase();
        newPreString = newPreString[0].toUpperCase() + newPreString.slice(1);
        newString += newPreString + "-"
    }

    return newString.slice(0, -1)
}

console.log(accum("ZpglnRxqenU"))