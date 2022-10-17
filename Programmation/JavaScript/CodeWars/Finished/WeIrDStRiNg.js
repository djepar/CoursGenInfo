function toWeirdCase(string){
    let wordsList = [];
    let oldString = string.split(" ")
    console.log(oldString)
    for (el of oldString){
        let newWord = ""
        for (let i = 0; i < el.length; i++){
            if (i % 2 == 0){
                newWord += el[i].toUpperCase();
            }
            else{
                newWord += el[i].toLowerCase();
          
            }
        }
        wordsList.push(newWord)
    }
    
    return wordsList.join(" ")
}
console.log(toWeirdCase("Bonjour la vie"))