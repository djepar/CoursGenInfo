"use strict";
(function(){
    document.getElementById("convert").addEventListener("submit", function(event){
        event.preventDefault();
        const distanceKM = parseFloat(document.getElementById("distance").value);
        //console.log(distanceKM)
        if (distanceKM ){
            const distanceMiles = (distanceKM * 1.609344).toFixed(3);
        //console.log(`distance in km ${distanceKM} distance miles : ${distanceMiles}`);
        var answerDiv = document.getElementById("answer");
        var newNode = document.createElement("h2");
        newNode.innerText =(`The distance is ${distanceMiles}`)
        answerDiv.replaceChild(newNode, answerDiv.children[0])
        }
        else{
            alert("You need to put a number! ")
        }
    })

})()