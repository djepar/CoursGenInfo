"use strict";
(function(){
    var ConvertTo =  1.609344 // Miles by default   
    var heading = document.querySelector("h1");
    var intro = document.querySelector("p");
    document.addEventListener("keydown", function(event){ var key = event.code; 
        if (key === "KeyK"){
            heading.innerHTML = "Kilometers to Miles Converter";
            intro.innerHTML =("Type in a number of kilometers and click the button to convert the distance to miles.");
            ConvertTo = 0.6213712;
        } else if (key == "KeyM") {
            heading.innerHTML = "Miles to Kilometers Converter";
            intro.innerHTML = ("Type in a number of miles and click the button to convert the distance to kilometers.");
            ConvertTo =  1.609344;
        }
    })
    //ConvertTo should be equal to either Miles or Kilometers
    document.getElementById("convert").addEventListener("submit", function(event){
        event.preventDefault();
        const distanceToConvert = parseFloat(document.getElementById("distance").value);
        //console.log(distanceKM)
        if (distanceToConvert){
            const distanceConverted = (distanceToConvert *ConvertTo).toFixed(3);
            
        //alert(`convertTo ${ConvertTo}, distanceToConvert = ${distanceToConvert}, distanceConverted ${distanceConverted} `)
        //console.log(`distance in km ${distanceKM} distance miles : ${distanceMiles}`);
        var answerDiv = document.getElementById("answer");
        var newNode = document.createElement("h2");
        newNode.innerText =(`The distance is ${distanceConverted}`)
        answerDiv.replaceChild(newNode, answerDiv.children[0])
        }
        else{
            alert("You need to put a number! ")
        }
    })


})()