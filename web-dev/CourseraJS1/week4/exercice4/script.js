(function(){
    var detailsForm = document.querySelector("#destination_details_form")
    detailsForm.addEventListener("submit", handleFormSubmit);

    function handleFormSubmit(event) {
        event.preventDefault();
        // 1. extract the value from each form field
        var destName = event.target.elements["name"].value;
        var destLocation = event.target.elements["location"].value;
        var destPhoto = event.target.elements["photo"].value;
        console.log(event.target.elements["description"].value);
        var destDescription = event.target.elements["description"].value;

        //2. clear out the form fields
        for (var i = 0; i < detailsForm.length; i++){
            detailsForm.elements[i].value = "";
        }

        //  3. Run a function that creates the new card
        var whishlistContainer = document.getElementById("title");

        if (whishlistContainer.children.length === 0) {
            document.getElementById("title").innerHTML = "My Whish List";


        }
        var destCard = createDestinationCard(destName, destLocation, destPhoto, destDescription);
        document.querySelector("#destinations_container").appendChild(destCard)
    }

    function createDestinationCard(name, location, photoUrl, description) {
        var card = document.createElement("div");
        card.className = "card";

        var img = document.createElement("img");
        img.setAttribute("alt", name);

        var constantPhotoUrl = 'images/signpost.jpg';

        if(photoUrl.length === 0){
            img.setAttribute('src', constantPhotoUrl);
        }
        else {
            img.setAttribute('src', photoUrl);
        }

        card.appendChild(img);

        var cardBody = document.createElement("h3");
        cardBody.className = "card-body";

        var cardTitle = document.createElement('h3');
        cardTitle.innerText = name;
        cardBody.appendChild(cardTitle);

        var cardSubtitle = document.createElement("h4");
        cardSubtitle.innerText = location;
        cardBody.appendChild(cardSubtitle);

        if (description.length !== 0) {
            var cardText = document.createElement("p");
            cardText.className = "card-text";
            cardText.innerText = description;
            cardBody.appendChild(cardText)

            
        }
        var cardDeleteBtn = document.createElement("button");
        cardDeleteBtn.innerText = "Remove";

        cardDeleteBtn.addEventListener("click", removeDestination);
        cardBody.appendChild(cardDeleteBtn)

        card.appendChild(cardBody)

        return card;

    }   
    function removeDestination(event) {
        var card = event.target.parentElement.parentElement;
        card.remove();
    }


    

}
)()