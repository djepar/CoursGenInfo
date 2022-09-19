
function upDate(previewPic){

    DivImage = document.getElementById("image");
    DivImage.style.backgroundImage="url("+previewPic.src+")";
    DivImage.innerHTML= previewPic.alt; 
    
}

	function unDo(){

    DivImage = document.getElementById("image");
    DivImage.style = "image";
    DivImage.innerHTML = "Hover over an image below to display here."
}