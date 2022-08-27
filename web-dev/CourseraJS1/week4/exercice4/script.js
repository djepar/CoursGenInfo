(function(){
    var detailsForm = document.querySelector("#destination_details_form")
    detailsForm.addEventListener("submit", handleFormSubmit);

    function handleFormSubmit(event) {
        event.preventDefault();
        // 1. extract the value from each form field
        const destName = event.target.elements["name"].value;
        const destLocation = event.target.elements["location"].value;
        const destPhoto = event.target.elements["photo"].value;
        const destDescription = event.target.elements["description"].value;

        //2. clear out the form fields
        for (let i = 0; i < detailsForm.length; i++){
            detailsForm.elements[i].value = "";
        }

        //  3. Run a function that creates the new card
        const whishlistContainer = document.getElementById("title");

        if (whishlistContainer.children.length === 0) {
            document.getElementById("title").innerHTML = "My Whish List";


        }
        const destCard = createDestinationCard(destName, destLocation, destPhoto, destDescription);
        document.querySelector("#destinations_container").appendChild(destCard)
    }

    function createDestinationCard(name, location, photoUrl, description) {
        const card = document.createElement("div");
        card.className = "card";

        const img = document.createElement("img");
        img.setAttribute("alt", name);

        const constantPhotoUrl = 'images/signpost.jpg';

        if(photoUrl.length === 0){
            img.setAttribute('src', constantPhotoUrl);
        }
        else {
            img.setAttribute('src', photoUrl);
        }

        card.appendChild(img);

        const cardBody = document.createElement("h3");
        cardBody.className = "card-body";

        const cardTitle = document.createElement('h3');
        cardTitle.innerText = name;
        cardBody.appendChild(cardTitle);

        const cardSubtitle = document.createElement("h4");
        cardSubtitle.innerText = location;
        cardBody.appendChild(cardSubtitle);

        if (description.length !== 0) {
            const cardText = document.createElement("p");
            cardText.className = "card-text";
            cardText.innerText = description;
            cardBody.appendChild(cardText)

            
        }
        const cardDeleteBtn = document.createElement("button");
        cardDeleteBtn.innerText = "Remove";

        cardDeleteBtn.addEventListener("click", removeDestination);
        cardBody.appendChild(cardDeleteBtn)

        card.appendChild(cardBody)

        return card;

    }   
    function removeDestination(event) {
        const card = event.target.parentElement.parentElement;
        card.remove();
    }


    

}
)()