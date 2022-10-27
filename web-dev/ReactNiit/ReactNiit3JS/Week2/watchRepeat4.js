// Chaining filter(), map(), reduce()
// Remove non premium product (price < 300)
// Convert all non-premium product to upper case
// Calculate stock of each Non-Premium product type
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
    ["Bow2", 500],
    ["Axe2", 50],
    ["Super2 Sword", 25000000000000000000000000000000.1],
    ["Sword2", 25],
    ["Bow3", 500],
    ["Axe3", 50],
    ["Super3s Sword", 25000000000000000000000000000000.1],
    
]

const nonPremiumProducts = products.filter(product => product[1]<=300)
    .map(prod=>[prod[0].toUpperCase(),prod[1]])
    .reduce((stocks, currentProduct)=>{
        let stockItem = stocks.find(item=>item[0]==currentProduct[0]);
        if(!stockItem){
            stocks.push([currentProduct[0],1]);
        }
        else {
            stockItem = ++stockItem[1];
        };
        return stocks
    }, [])
console.log(nonPremiumProducts)
const PremiumProducts = products.filter(product => product[1]>=300)
    .map(prod=>[prod[0].toUpperCase(),prod[1]])
    .reduce((stocks, currentProduct)=>{
        let stockItem = stocks.find(item=>item[0]==currentProduct[0]);
        if(!stockItem){
            stocks.push([currentProduct[0],1]);
        }
        else {
            stockItem = ++stockItem[1];
        };
        return stocks
    }, [])
console.log(PremiumProducts)