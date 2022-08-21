"use strict";
bonjour = 0;
(function(){

    var currentImage = 0;
    var myphotos = ['image1.jpg','image2.jpg', 'image3.jpg','image4.jpg', 'image5.jpg']
    var container = document.getElementById('content');
    var nextBtn = document.getElementById('next');
    var prevBtn = document.getElementById("previous");

    nextBtn.addEventListener("click", function(event){

        event.preventDefault();
        currentImage++;
        if (currentImage > myphotos.length -1) {currentImage = 0}
        swapImg();
    })
    prevBtn.addEventListener("click", function(event){
        event.preventDefault();
        currentImage--;
        if (currentImage < 0){currentImage = myphotos.length -1}
    
        swapImg();
     
    })
    function swapImg(){
        var newSlide = document.createElement('img');
        newSlide.src = `slides/${myphotos[currentImage]}`;
        newSlide.className = "fadeinimg";
        container.appendChild(newSlide);
        if (container.children.length > 2){
        container.removeChild(container.children[0])
    }
    }
    console.log(bonjour)
})()
