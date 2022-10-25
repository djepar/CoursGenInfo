// Write the Js function to get the prices post deduction of given discount for a given array of products prices

const products = [
    ["Sword", 25],
    ["Bow", 500],
    ["Axe", 50],
    ["Super Sword", 25000000000000000000000000000000.1],
    
]

const calculateDiscountPrice = discount => products.map(
    product => [product[0], product[1]-product[1]*discount/100]
)


// const calculateDiscountPrice = discount => {
//     for(let i = 0; i < products.length;i++){
//         products[i][1] = products[i][1] - products[i][1] * discount/100;
//     }
// }
let discount = calculateDiscountPrice(10);
console.log(products)