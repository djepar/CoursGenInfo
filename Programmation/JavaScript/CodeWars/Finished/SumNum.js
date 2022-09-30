function SigmaSummation(a,b){
    if (a>b){
        big = a;
        small = b;
    } else { big = b; small = a;}
    let sum = 0;
    for (let i = small; i <= big; i++){
        sum+= i;
    }
    return sum
}

const func = (a,b) => (a == b) ? a : SigmaSummation(a,b);

console.log(func(1, 6))
console.log((6-1+1)*7 /2)

// Easier would be (max - min + 1) * (min + max) / 2; or (Math.abs(a - b) + 1) * (a+b) / 2;