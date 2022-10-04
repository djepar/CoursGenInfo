const arr = (n = 0) => [...Array(n).keys()]

const arr2 = N => [...Array(N || 0).keys()]
arr

console.log(arr(10))
console.log(arr2(100))
console.log(Array(5))