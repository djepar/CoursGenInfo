function titleCase(title, minorWords) {
    if (title == ""){
        return ""
      }
    let titleList = title.split(" ");
    let finalList = []
    let minor = minorWords.toLowerCase();

    for (let i = 0; i < titleList.length; i++){
        let newword = ""
       
        if (i == 0){
            newword += titleList[i][0].toUpperCase();
            newword += titleList[i].substr(1,).toLowerCase();
        } else if(minor.indexOf(titleList[i].toLowerCase()) >= 0){
            newword += titleList[i].toLowerCase();
        } else {
            newword += titleList[i][0].toUpperCase();
            newword += titleList[i].substr(1,).toLowerCase();
        }
        finalList.push(newword);

    }
    return finalList.join(" ")
}

console.log(titleCase('a clash of KINGS', 'a an the of'))

console.log(titleCase('THE WIND IN THE WILLOWS', 'The In'))