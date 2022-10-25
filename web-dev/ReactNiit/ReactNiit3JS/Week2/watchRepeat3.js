// for the given array of product with prices, write the JS function to filter out the premium products.
//Products with price above 300, are marked as premium Products
//Apply a 15% discount on all the non-premium products.
// Create a stock of each product type.

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
const premiumItems = products.filter(item => item[1] > 300);
console.log("premiumItems", premiumItems);
const filteredProd = products.filter(item => item[1] <= 300)
console.log("filteredProd", filteredProd)

const nonPremium = filteredProd.map(product => [product[0], product[1] - product[1]*0.15]  );
console.log("nonpremium", nonPremium);
//products.map(item => item[1] < 300 ? item[1]-(item[1]*0.15) : item);
//console.log(result)

let stocksResult = products.reduce((stocks, product)=>{
    let stockItem = stocks.find(stock => stock[0] == product[0]);
    if (!stockItem){
        stocks.push([product[0], 1])
    } else {
        stockItem[1]++
    }
    return stocks
},[])

let stocks = []
console.log(stocksResult);
