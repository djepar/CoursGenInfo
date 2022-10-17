function findUniq(arr) {
    for(let i = 0; i < arr.length; i++){
        if (arr[i] !== arr[i+1]){
            if (arr[i] !== arr[i-1] |arr[i] !== arr[i+1]){
                return arr[i]

            }
        }
    
    }
    
}
console.log(findUniq([ 0, 0, 1]))