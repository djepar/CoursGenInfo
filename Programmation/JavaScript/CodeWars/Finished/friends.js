let friend = friends => {
    const pattern = /^[a-zA-Z]{4}$/;

    let newlist = []
    for (el of friends){
        console.log(`el : ${el} = ${pattern.test(el)}`)
        if (pattern.test(el)){
            newlist.push(el);
        }
    }
    return newlist
}

console.log(friend(["Ryan", "Kieran", "Mark", "Tim"]))