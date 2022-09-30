function BruteForce(list, target){
    for(let i = 0; i < list.length; i++){
        for (let j = i+1; j < list.length; j++){
            if (list[i] + list[j] == target){
                return [i, j]
            }
        }
    }
    
}

console.log(BruteForce([1,2,3,4,5,6,7], 3))

console.log(typeof (BruteForce([1,2,3,4,5,6,7], 10)))
