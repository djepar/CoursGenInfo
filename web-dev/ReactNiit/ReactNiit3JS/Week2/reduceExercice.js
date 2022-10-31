
const products = [
    ["Sword", 25],
    ["Bow", 500],
    ["Axe", 50],
    ["Super Sword", 41.1],
    ["Sword2", 25],
    ["Bow2", 500],
    ["Axe2", 50],
    ["Sword2", 25],
    ["Bow2", 500],
    ["Axe2", 50],
    ["Sword2", 25],
    ["Superbonjour", 800],
    ["Axe2", 50],
    ["Super2 Sword", 1],
    ["Sword2", 25],
    ["Bow3", 500],
    ["Axe3", 50],
    ["Super3s Sword", 1],
    
]
// Sum of everything
let initalvalue = 0
let newprod = products.reduce((acc, product)=> acc + product[1], 0
);
//console.log(newprod)

//Create a list of all the item
let newprod2 = products.reduce((acc, product) => [...acc, product[0]], []);
//console.log(newprod2)


//Create a dictionary of all the item
let count = 0;
let newprod3 = products.reduce((acc, product) => {
    count++
    return {...acc, [count] : product};
}, {});
//console.log(newprod3)


// Find the biggest number
result = products.reduce((acc, product) => {
    if (acc === null || product[1]> acc) return product[1];
    return acc;
}, null);
console.log(result)

result2 = products.reduce((acc, product) => {
    if (acc === null || product[1] < acc) return product[1];
    return acc;
}, null);
//console.log(result2)

// find by name
result3 = products.reduce((acc, product) => {
    if (acc !== null) return acc;
    if (product[0] === "Superbonjour") return product;
    return null
}, null);

//console.log(result3)

// if all over 18
result4 = products.reduce((acc, product) => {
    if(!acc) return false;
    return product[1] >= 1;
}, true);
//console.log(result4)

// if one is over 400
result4 = products.reduce((acc, product) => {
    if(acc) return true;
    return product[1] > 600;
}, false);
//console.log(result4)

const orders = [
    {id: "1", "status": "pending"},
    {id: "2", "status": "pending"},
    {id: "3", "status": "cancelled"},
    {id: "4", "status": "shipped"},
    {id: "5", "status": "pending"},
    {id: "6", "status": "pending"},
    {id: "7", "status": "cancelled"},
    {id: "8", "status": "shipped"},
    {id: "9", "status": "pending"},
    {id: "10", "status": "pending"},
    {id: "11", "status": "cancelled"},
    {id: "12", "status": "shipped"},
    {id: "13", "status": "pending"},
    {id: "14", "status": "pending"},
    {id: "15", "status": "cancelled"},
    {id: "16", "status": "shipped"},
    {id: "17", "status": "pending"},
    {id: "18", "status": "pending"},
    {id: "19", "status": "cancelled"},
    {id: "20", "status": "shipped"},
]

//calculating the number of each order
result5 = orders.reduce((acc, order)=>{
    return{...acc, [order.status]: (acc[order.status] || 0) +1}
}, {})
//console.log(result5)

// flatten
const folders = [
    "index.js",
    ["flatten.js", "map.js"],
    ["any.js", ["afer.js", "count.js"]],
];

function flatten(acc, item) {
    //console.log(acc,item)
    if (Array.isArray(item)){
        return item.reduce(flatten, acc);
    }
    return [...acc, item];
}

result6 = folders.reduce(flatten, []);
console.log(result6)

// create reduce ourselves
function reduce2(array, callback, initial){
    let acc = initial;
    for (let i = 0; i < array.length; i++){
        acc = callback(acc, array[i], i, array);
    }
    return acc;
}
result7 = reduce2([1,2,3], (acc, num) => acc+num, 0);
console.log(result7)