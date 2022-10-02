 function twoSum(list, target){
    //console.log(`List length is  : ${list.length}, target = ${target}`)
    for(let i = 0; i < list.length; i++){
        for (let j = 1; j < list.length; j++){
            //console.log(`i = ${i} list[i] = ${list[i]}, j = ${list.length - j}, list[-j] = ${list[list.length - j]}`)
            //console.log(`${list[i]} + ${list[list.length - j]} = ${list[i] + list[list.length - j]}`)
            if (list[i] + list[list.length - j] == target && (i != (list.length - j))){
                
                return [i, (list.length - j)]
            }
        }
    }
    
}

console.log(twoSum([2,3,4],7))
console.log(twoSum([1,2,3,4], 6))
console.log(twoSum([3,6,7,8], 15))